from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post
from users.models import Profile
from polls.models import Questions

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'post_type']

class UpdateUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

class CreatePetitionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question']

