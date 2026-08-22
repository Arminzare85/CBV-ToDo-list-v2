from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','priority']
        widgets = {
            'priority': forms.Select(choices=[(1,'Low'),(2,'Low'),(3,'Low'),(4,'Medium'),(5,'Medium'),(6,'Medium'),(7,'Medium'),(8,'High'),(9,'High'),(10,'High')])
        }