from django.contrib import admin
from django.urls import path 
from django.views.generic import TemplateView
from .views import IndexView , TaskListView , CreateTaskView , UpdateTaskView , DeleteTaskView

app_name = 'list'

urlpatterns = [
    path('',TaskListView.as_view(),name='index'),
    path('create/',CreateTaskView.as_view(),name='create'),
    path(
    'update/<int:pk>/',UpdateTaskView.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteTaskView.as_view(),name='delete'),
]