from django.contrib import admin
from django.urls import path, include
import users
import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('main.urls')),
]

