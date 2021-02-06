from django.views import View
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import UpdateView, DeleteView

from .models import Task
from .forms import *

# Create your views here.


class TodoView(View):
    form_class = TaskForm
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all().order_by("-created")
        form = self.form_class

        context = {}
        context['form'] = form
        context["tasks"] = tasks

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect(reverse('todo-list'))

        return render(request, self.template_name, {'form': form})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "app/update.html"
    success_url = reverse_lazy("todo-list")

# class TaskUpdateCheckView(UpdateView):
#     model = Task
#     form_class = TaskUpdateCheckForm
#     template_name = "app/update.html"
#     success_url = reverse_lazy("todo-list")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "app/delete.html"
    success_url = reverse_lazy("todo-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.get(pk=self.kwargs["pk"])
        return context


def CheckView(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskUpdateCheckForm(instance=task)

    if request.method == 'POST':
        form = TaskUpdateCheckForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo-list'))