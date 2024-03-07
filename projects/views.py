from django.shortcuts import render
from projects.models import Project

# Create your views here.
def all_projects(request):
    # Query the DataBase
    project = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'project':project})

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/proj_details.html', {'project':project})


