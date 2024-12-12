from django.urls import path
from . import views


#urls for all HTML pages
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/', views.edit_task, name='edit_task'),
    path('remove/', views.remove_task, name='remove_task'),
    path('view_task/<str:status>/', views.view_tasks, name='view_tasks'),
]
