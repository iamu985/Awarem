from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    question = models.TextField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question
