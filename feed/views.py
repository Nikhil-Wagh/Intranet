# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Project

# from django.template import loader

# Create your views here.
app_name = 'feed'


def index(request):
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects}
    return render(request, 'feed/index.html', context)
    # template = loader.get_template('feed/index.html')
    # return HttpResponse(template.render(context, request))


    # html = ' '
    # for project in all_projects:
    #     url = '/feed/' + str(project.id) + '/'
    #     html += '<a href="' + url + '">' + project.name + '</a><br>'
    # return HttpResponse(html)


def detail(request, project_id):
    # try:
    #     project = Project.objects.get(pk = project_id)
    # except Project.DoesNotExist:
    #     raise Http404("Project does not exist.")
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'feed/detail.html', {'project': project})

    # class feed_sitemap(Sitemap):
    #     changefreq = "daily"
    #     priority = 1.0
    #     lastmod = datetime.datetime.now()
    #     def items(self):
    #         return Project.objects.all()
