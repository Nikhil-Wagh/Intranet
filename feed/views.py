# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from .models import Project


#from django.template import loader

# Create your views here.

def index(request):
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects}
    return render(request, 'feed/index.html', context)
    #template = loader.get_template('feed/index.html')
    #return HttpResponse(template.render(context, request))


    # html = ' '
    # for project in all_projects:
    #     url = '/feed/' + str(project.id) + '/'
    #     html += '<a href="' + url + '">' + project.name + '</a><br>'
    #return HttpResponse(html)

def detail(request, project_id):
    try:
        project = Project.objects.get(pk = project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")
    return render(request, 'feed/detail.html', {'project': project})