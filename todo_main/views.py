from django.shortcuts import render
from todo.models import Task
def home(request):
    Completedtasks=Task.objects.filter(Is_completed=False)
    context={'Completedtasks':Completedtasks}
    return render(request,'home/home.html',context)

