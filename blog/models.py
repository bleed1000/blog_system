from django.db import models

#from users.models import User

class Blog(models.Model):
    title = models.CharField('Title', max_length=200)

    def __str__(self):
        return self.title
    
    class Meta():
        db_table = 'blog'
        verbose_name = "Блог"
        verbose_name_plural = 'Блоги'

class PostBody(models.Model):
    image = models.ImageField(blank=True, null=True, verbose_name='Картинка')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"PostBody: {self.text[:20]}"

    class Meta:
        db_table = 'post_body'
        verbose_name = "Тело поста"
        verbose_name_plural = 'Тела постов'


class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    post_body = models.ForeignKey(PostBody, verbose_name="Тело Поста", on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return f"Post by {self.user.username} in blog {self.blog.title}"

    def total_likes(self):
        return self.reactions.filter(reaction_type=Reaction.LIKE).count()
    
    def total_dislikes(self):
        return self.reactions.filter(reaction_type=Reaction.DISLIKE).count()

    class Meta:
        db_table = 'post'
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'

class Reaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'

    REACTION_CHOICES = [
        (LIKE, 'like'),
        (DISLIKE, 'dislike'),
    ]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} - {self.reaction_type} on {self.post.id}"