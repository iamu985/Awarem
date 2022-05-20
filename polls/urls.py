from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('index/', views.polls_list_view, name="polls"),
    path('details/<int:question_id>', views.polls_detail_view, name='details'),
    path('vote/<int:question_id>', views.polls_vote_view, name="vote"),
    path('petition-create/', views.polls_petition_create_view, name="petition-create")
]