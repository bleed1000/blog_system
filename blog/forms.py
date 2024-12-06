from django import forms
from django.db.models import CharField, TextField
from blog.models import Blog, Post, PostBody, Reaction
from django.forms import ModelForm, TextInput, Textarea

class BlogForm(ModelForm):

    title = forms.CharField()

    class Meta:
        model = Blog
        fields = ['title']

class PostForm(ModelForm):
    class Meta:
        model = PostBody
        fields = ['text', 'image']

    def save(self, user, blog, commit=True):
        # Сначала сохраняем PostBody
        post_body = super().save(commit=False)
        if commit:
            post_body.save()
        
        # Теперь создаем Post, используя post_body и связывая с блогом и пользователем
        post = Post.objects.create(
            user=user,
            post_body=post_body,
            blog=blog,
        )
        return post
    


class ReactionForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.HiddenInput)
    reaction_type = forms.ChoiceField(choices=Reaction.REACTION_CHOICES, widget=forms.HiddenInput)
        