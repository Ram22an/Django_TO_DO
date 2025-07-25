from django.shortcuts import render
from todo.models import Task
def home(request):
    NotCompletedtasks=Task.objects.filter(Is_completed=False).order_by('updated_at')
    Completedtasks=Task.objects.filter(Is_completed=True).order_by('updated_at')
    context={'NotCompletedtasks':NotCompletedtasks,
             'CompletedTasks':Completedtasks}
    return render(request,'home/home.html',context)

