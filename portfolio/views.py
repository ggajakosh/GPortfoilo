from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from rest_framework import viewsets
from .serializers import ProjectSerializer


# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('title')
    serializer_class = ProjectSerializer
