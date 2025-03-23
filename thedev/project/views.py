from django.shortcuts import render

from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})


def project_details(request, pk):
    # how to get the project id from the URL
    project = Project.objects.get(id=pk)
    return render(request, 'project/project_details.html', {'project': project})
