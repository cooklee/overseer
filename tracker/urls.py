"""
URL configuration for overseer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tracker import views

urlpatterns = [
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),
    path('projects/', views.ShowProjectsView.as_view(), name='projects'),
    path('task/<int:id>/', views.ShowTaskDetailView.as_view(), name='task_detail'),
    path('add_timespent/', views.AddTimeSpendToTaskView.as_view(), name='add_timespent'),
    path('add_cost_to_task/<int:task_id>/', views.AddCostToTimeSpentView.as_view(), name='add_cost_to_task'),
    path('add_resource/', views.AddResourceView.as_view(), name='add_resource'),
    path('resource/<int:pk>/', views.DetailResourceView.as_view(), name='detail_resource'),
    path('delete_resource/<int:pk>/', views.DeleteResourceView.as_view(), name='delete_resource'),
    path('update_resource/<int:pk>/', views.UpdateResourceView.as_view(), name='update_resource'),

    path('list_resource/', views.ListResourceView.as_view(), name='list_resource')
]
