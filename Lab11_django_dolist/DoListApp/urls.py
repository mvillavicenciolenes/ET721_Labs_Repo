# DoListApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                        # Home page
    path('add/', views.add_task, name='add_task'),              # URL for adding tasks
    path('delete_all_completed/', views.delete_all_completed, name='delete_all_completed'),  # URL for deleting all completed tasks
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),  # URL for marking task complete
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')         # URL for deleting a specific task
]