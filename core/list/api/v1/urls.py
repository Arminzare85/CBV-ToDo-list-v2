from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TaskModelViewSet
from .schema import openapi_schema


router = DefaultRouter()

router.register(
    'task',
    TaskModelViewSet,
    basename='task'
)

urlpatterns = [
    path('schema/', openapi_schema, name='schema'),
]

urlpatterns += router.urls