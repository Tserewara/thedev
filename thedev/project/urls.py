from django.urls import path

from .views import project_details, project_list

urlpatterns = [
    path('', project_list, name='project_list'),
    path('projects/<int:pk>/', project_details, name='project_details'),
]
