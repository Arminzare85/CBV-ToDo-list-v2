from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','priority','is_completed','created_at')
    list_filter = ('priority','is_completed')
    search_fields = ('title','description')
admin.site.register(Task,TaskAdmin)