

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from tracker.forms import AddTimeSpentToTaskForm, AddCostToTaskForm
from tracker.models import Task, TimeSpent, Resource


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AddTaskView(View):

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'form.html', {'tasks': tasks})

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


class ShowProjectsView(View):

    def get(self, request):
        projects = Task.objects.filter(parent__isnull=True)
        return render(request, 'projects.html', {'projects': projects})


class ShowTaskDetailView(View):

    def get(self, request, id):
        task = Task.objects.get(id=id)
        form = AddCostToTaskForm()
        return render(request, 'task_detail.html', {'task': task, 'form':form})

    def post(self, request, id):
        name = request.POST.get('name')
        description = request.POST.get('description')
        parent = Task.objects.get(id=id)
        Task.objects.create(name=name, description=description, parent=parent)
        return redirect('task_detail', id)

class AddCostToTimeSpentView(View):

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        form = AddCostToTaskForm(request.POST)
        if form.is_valid():
            cost = form.save(commit=False)
            cost.task=task
            cost.save()
            return redirect('task_detail', task.id)
class AddTimeSpendToTaskView(View):
    def get(self, request):
        form = AddTimeSpentToTaskForm()
        return render(request, 'form_new.html', {'form':form})


    def post(self, request):
        form = AddTimeSpentToTaskForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount'] # to juz bedzie int
            task = form.cleaned_data['task']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            TimeSpent.objects.create(amount=amount, task=task, date=date, description=description)
            return redirect('add_timespent')
        else:
            return render(request, 'form_new.html', {'form':form})


class AddResourceView(CreateView):
    model = Resource
    fields = '__all__'
    template_name = 'form_generic.html'

    # success_url = reverse_lazy('add_resource')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources'] = Resource.objects.all()
        return context

    # def form_valid(self, form):
    #     super(AddResourceView, self).form_valid()
    #
    # def form_invalid(self, form):
    #     pass
    def get_success_url(self):
        return reverse('detail_resource', args=(self.object.pk,))

class DetailResourceView(DetailView):
    model = Resource
    template_name = 'detail_resource.html'


class DeleteResourceView(DeleteView):
    model = Resource
    template_name = 'delete_form.html'
    success_url = reverse_lazy('list_resource')


class UpdateResourceView(UpdateView):
    model = Resource
    fields = '__all__'
    template_name = 'form_generic.html'
    success_url = reverse_lazy('list_resource')


class ListResourceView(ListView):
    model = Resource
    template_name = 'list_view.html'

