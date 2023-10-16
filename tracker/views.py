from django.shortcuts import render, redirect
from django.views import View

from tracker.models import Task


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AddTaskView(View):

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'form.html', {'tasks':tasks})

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        parent_id = request.POST.get('parent', '')
        if parent_id == '':
            parent = None
        else:
            parent = Task.objects.get(id=parent_id)
        Task.objects.create(name=name, description=description, parent=parent)
        return redirect('add_task')