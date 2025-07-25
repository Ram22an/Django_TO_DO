from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,id):
    task=get_object_or_404(Task,id=id)
    task.Is_completed=True
    task.save()
    return redirect('home')
def deleteTask(request,id):
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect('home')
def Mark_as_not_done(request,id):
    task=get_object_or_404(Task,id=id)
    task.Is_completed=False
    task.save()
    return redirect('home')
def editTask(request,id):
    task_obj=get_object_or_404(Task,id=id)
    if request.method=='POST':
        task=request.POST['task']
        task_obj.task=task
        task_obj.save()
        return redirect('home')
    if request.method=='GET':
        return render(request,'editTask/editTask.html',{'task_obj':task_obj})

