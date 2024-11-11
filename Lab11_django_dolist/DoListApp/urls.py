from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                        
    path('add/', views.add_task, name='add_task'),              
    path('delete_all_completed/', views.delete_all_completed, name='delete_all_completed'),  
    path('delete_all/', views.delete_all, name='delete_all'),  
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),  
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')         
]
