from blog.models import Post, PostBody
from django.shortcuts import get_object_or_404

class PostService:

    def add_post(self, user, blog, text, image=None):
        post_body = PostBody.objects.create(text=text, image=image)

        post = Post.objects.create(user=user, blog=blog, post_body=post_body)

        return post

    def delete_post(self, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()

    def update_post(self, post_id, text=None, image=None):
        post = get_object_or_404(Post, id=post_id)

        if text is not None:
            post.post_body.text = text
        if image is not None:
            post.post_body.image = image
        
        post.post_body.save()

        return post

    def get_post(self, post_id):
        post = get_object_or_404(Post, id=post_id)
        return post