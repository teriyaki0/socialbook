from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    userPost = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Post by", default="", null=True)
    content = models.TextField('Контент')
    postDate = models.DateTimeField('Дата публикации', default=datetime.now)
    image = models.ImageField(upload_to='post_image', blank=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("postDetail", args=[self.pk])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField('Дата коммента', default=datetime.now)

    def __str__(self):
        return self.text
