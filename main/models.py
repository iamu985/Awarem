from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    POST_TYPES  = (
        ("P", "Petition"),
        ("E", "Event"),
        ("C", "Charity"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=500)
    date_published = models.DateTimeField(default=timezone.now)
    upvote = models.IntegerField(default=0, null=True)
    downvote = models.IntegerField(default=0, null=True)
    post_type = models.CharField(max_length=1, choices=POST_TYPES)

    def __str__(self):
        return self.title

class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.BooleanField(null=True)
    
    def __str__(self):
        return f"{self.user}:{self.post}:{self.value}"
    

