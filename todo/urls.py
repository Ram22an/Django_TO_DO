from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:id>',views.mark_as_done,name='mark_as_done'),
    path('deleteTask/<int:id>',views.deleteTask,name='deleteTask'),
]