
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=108)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta():
        ordering = ["-post_date"]

    def __str__(self):
        return self.title
