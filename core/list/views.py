from django.shortcuts import render
from django.views.generic import TemplateView , ListView , CreateView , UpdateView , DeleteView
from .models import Task
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import get_object_or_404

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['task_priorities'] = Task._meta.get_field(
            'priority'
        ).choices

        return context
    def get_queryset(self):
        return Task.objects.all().order_by('-priority')

class CreateTaskView(CreateView):
    model = Task
    fields = ['title', 'description', 'priority']
    template_name = 'index.html'
    success_url = '/todo/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tasks'] = Task.objects.all()
        context['task_priorities'] = Task._meta.get_field(
            'priority'
        ).choices

        return context
class UpdateTaskView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        task.is_completed = not task.is_completed
        task.save()

        return redirect('list:index')


class DeleteTaskView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('list:index')