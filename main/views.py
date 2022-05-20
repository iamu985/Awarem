from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Preference
from .forms import PostForm, UpdateProfileForm, UpdateUserForm, CreatePetitionForm
from django.http import HttpResponse
# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    posts = Post.objects.all()
    petition_form = CreatePetitionForm()
    if request.method == "POST":
        form = CreatePetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:polls')
    context = {"user":user, "posts":posts, 'petition_form':petition_form}
    return render(request, "main/dashboard.html", context)

@login_required
def make_post(request):
    user = request.user
    post_form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = user
            new_post.save()
            context = {'users':user}
            return redirect("main:dashboard")
    context = {"post_form":post_form, "user":user}
    return render(request, "main/post_create.html", context)

@login_required
def profile_update(request):
    user = request.user
    update_profile_form = UpdateProfileForm()
    update_user_form = UpdateUserForm()
    update_user_form.initial['first_name'] = user.first_name
    update_user_form.initial['last_name'] = user.last_name
    update_user_form.initial['username'] = user.username
    update_user_form.initial['email'] = user.email
    update_profile_form.initial['bio'] = user.profile.bio
    if request.method == "POST":
        profile_form = UpdateProfileForm(request.POST, instance=request.user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            print('PROFILE FORM IS VALID')
            profile_form.save()
            # print("Profile is saved")
        if user_form.is_valid():
            print('USER FORM IS VALID')
            user_form.save()
            context = {"user":request.user}
            return redirect("main:profile_view")
    context = {'profile_update_form':update_profile_form, 'user_update_form':update_user_form}
    return render(request, "main/profile-update.html", context)

@login_required
def profile_view(request):
    context = {"user":request.user}
    return render(request, "main/profile-view.html", context)
