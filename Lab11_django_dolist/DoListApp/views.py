# DoListApp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDolist

def index(request):
    todo_tasks = ToDolist.objects.order_by('id')
    context = {'todo_tasks': todo_tasks}
    return render(request, 'index.html', context)

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('text')
        if task_text:
            ToDolist.objects.create(text=task_text)
        return redirect('index')

def delete_all_completed(request):
    ToDolist.objects.filter(completed=True).delete()
    return redirect('index')

def complete_task(request, task_id):
    task = get_object_or_404(ToDolist, id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(ToDolist, id=task_id)
    task.delete()
    return redirect('index')