# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Project, Module, Commit, Comment

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
    module=get_object_or_404(Module, pk=module_id)
    p = Project.objects.filter(module=module)
    project_id = p[0].id
    all_commits = Commit.objects.filter(module_id = module_id)
    context = {
        'all_commits': all_commits,
        'module': module,
        'project_id': project_id,
    }
    return render(request, 'feed/commit_detail.html', context)

def comment_detail(request, commit_id):
    commit = get_object_or_404(Commit, pk=commit_id)
    all_comments = Comment.objects.filter(commit_id = commit_id)
    context = {
        'all_comments': all_comments,
        'commit' : commit,
    }
    return render(request, 'feed/comment_detail.html', context)
