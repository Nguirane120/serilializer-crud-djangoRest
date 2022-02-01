from unicodedata import name
from django.urls import path, re_path
from .views import *
from . import views



urlpatterns = [
    path("", views.overview, name="Overview"),
    path("task-list/", views.taskList, name='task-liste'),
    path("task-detail/<str:pk>/", views.taskDetail, name='task-detail'),
    path("task-create/", views.taskCreate, name='create-task'),
    path("task-update/<str:pk>/", views.taskUpdate, name='task-update'),
    path("task-delete/<str:pk>/", views.taskDelete, name='task-deleted'),
]