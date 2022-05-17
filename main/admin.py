from django.contrib import admin
from .models import Post, Preference

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    fieldsets = [
        ("User", {'fields':["user"]}),
        ("Post", {'fields':["title", "body", "date_published"]}),
        ("Meta", {'fields':['post_type', 'upvote', 'downvote']}),
    ]

class PreferenceAdmin(admin.ModelAdmin):
    model = Preference
    fields = ["user", "post", "value"]

admin.site.register(Post, PostAdmin)
admin.site.register(Preference, PreferenceAdmin)
