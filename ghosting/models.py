from django.db import models


class Post(models.Model):
    boast = models.BooleanField()
    post = models.CharField(max_length=280)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    creation_time = models.DateTimeField(auto_now=True)
