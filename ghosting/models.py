from django.db import models
from django.utils import timezone


class Post(models.Model):
    boast = models.BooleanField()
    post = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    creation_time = models.DateTimeField(default=timezone.now())


    @property
    def total_votes(self):
        return self.up_votes - self.down_votes