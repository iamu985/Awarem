from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import users
import polls
        
app_name = "main"
urlpatterns = [
        path('', users.views.user_login, name="landing"),
        path('dashboard/', views.dashboard, name="dashboard"),
        path('post-create/', views.make_post, name="create_post"),
        path('profile-update/', views.profile_update, name="profile_update"),
        path('profile-view/', views.profile_view, name="profile_view"),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
