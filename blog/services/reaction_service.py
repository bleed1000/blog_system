from blog.models import Post, Reaction
from django.core.exceptions import ObjectDoesNotExist

class ReactionService:

    def add_reaction(self, user, post, reaction_type):
        reaction, created = Reaction.objects.get_or_create(
            user=user,
            post=post,
            defaults={'reaction_type': reaction_type}
        )
        if not created and reaction.reaction_type != reaction_type:
            reaction.reaction_type = reaction_type
            reaction.save()
        return reaction

    def delete_reaction(self, user, post):
        try:
            reaction = Reaction.objects.get(user=user, post=post)
            reaction.delete()
        except ObjectDoesNotExist:
            pass 

    def get_reaction(self, user, post):
        try:
            reaction = Reaction.objects.get(user=user, post=post)
            return reaction
        except ObjectDoesNotExist:
            return None
