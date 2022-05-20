from django.contrib import admin
from django.urls import path, include
import users
import main
import polls

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('users.urls')),
    path('', include('main.urls')),
    path('polls/', include('polls.urls')),
]

