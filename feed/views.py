# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Project, Module

# from django.template import loader

# Create your views here.
app_name = 'feed'


def index(request):
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects}
    return render(request, 'feed/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'feed/detail.html', {'project': project})


def commit_detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    return render(request, 'feed/commit_detail.html', {'module': module})


