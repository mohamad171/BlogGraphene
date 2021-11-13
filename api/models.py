from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

