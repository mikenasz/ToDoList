from django.shortcuts import render, redirect
from .models import todo
from .forms import TaskForm
from django.contrib import messages
def index(request):
    tasks = todo.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')
def complete_task(request, id):
    tasks = todo.objects.get(id=id)
    tasks.completed = True
    tasks.save()
    messages.success(request, tasks.task_name + " has been completed.")
    return redirect('index')
def update(request,id):
    tasks = todo.objects.get(id=id)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'todo/update.html', context)

def delete(request, id):

    tasks = todo.objects.get(id=id)


    if request.method == 'POST':
        messages.success(request, tasks.task_name + " has been removed.")
        tasks.delete()
        return redirect('index')
    context = { 'tasks': tasks}

    return render(request, 'todo/delete.html', context)