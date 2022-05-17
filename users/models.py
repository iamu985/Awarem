from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Post

from PIL import Image
import uuid
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="index.png", upload_to="profile_pic")
    bio = models.TextField(max_length=150, default="Your bio here!")
    follows = models.ManyToManyField(
        "self",
        related_name="follwed_by",
        symmetrical = False,
        blank = True,
    )
    
    # def save(self, *args, **kwargs):
    #     super().save()
    #     img = Image.open(self.profile_picture.path)
    #     if img.height > 200 and img.width > 200:
    #         new_img_size = (128, 128)
    #         img.thumbnail(new_img_size)
    #     img.save(self.profile_picture.path)
        

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
    

