from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from list.models import Task
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = {'priority':['exact'] , 'is_completed':['exact']}
    ordering_fields = ['published_time']
    search_fields = ['title', 'content']
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    pagination_class = CustomPagination