from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey, TextField

from blog.models import Post

class User(AbstractUser):
    nickname = CharField(max_length=20, blank=True)
    roles = models.JSONField(default=list, blank=True)
    image = models.ImageField(blank=True, null=True, verbose_name='Аватар')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

class TextComments(models.Model):
    text = TextField(null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    text = models.ForeignKey(TextComments, on_delete=models.CASCADE, related_name='text_comments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("blog.Post", on_delete=models.SET_NULL, related_name='comments', null=True, blank=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Comment by {self.user.username}: {self.text.text[:20]}"
    
