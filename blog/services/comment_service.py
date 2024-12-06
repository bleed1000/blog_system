from users.models import Comment, TextComments
from blog.models import Post
from django.shortcuts import get_object_or_404

class CommentService:

    def add_comment(self, user, post_id, text):
        post = get_object_or_404(Post, id=post_id)

        text_comment = TextComments.objects.create(text=text)

        comment = Comment.objects.create(user=user, text=text_comment, post=post)

        return comment

    def delete_comment(self, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
    
    def get_comments(self, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all() 
        return comments
