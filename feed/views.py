# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import ProjectForm, ModuleForm, CommitForm
from .models import Project, Module, Commit, Comment

app_name = 'feed'


def index(request):
    all_projects = Project.objects.all()
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, prefix="project")
        if project_form.is_valid():
            new_project = Project()
            new_project.name = project_form.cleaned_data['name']
            new_project.manager_id = project_form.cleaned_data['manager_id']
            new_project.description = project_form.cleaned_data['description']
            new_project.publish = timezone.now()
            new_project.save()
            return HttpResponseRedirect('/feed')

    else:
        project_form = ProjectForm(prefix='project')

    context = {'all_projects': all_projects,
               'project_form': project_form,
               'form_head': "Project",
               }
    return render(request, 'feed/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        module_form = ModuleForm(request.POST, prefix="module")
        if module_form.is_valid():
            try:
                new_module = Module()
                new_module.project_id = Project.objects.filter(id=project_id)[0]
                new_module.name = module_form.cleaned_data['name']
                new_module.description = module_form.cleaned_data['description']
                new_module.publish = timezone.now()
                new_module.save()
            except Exception as e:
                print(e)
            else:
                # print("New Module added", new_module.name, new_module.description)
                return HttpResponseRedirect('/feed')

    else:
        module_form = ModuleForm(prefix="module")

    return render(request, 'feed/detail.html', {'module_form': module_form,
                                                'form_head': "Module",
                                                'project':project,
                                              })


def commit_detail(request, module_id):
    mod = get_object_or_404(Module, pk=module_id)
    p = Project.objects.filter(module=mod)
    project_id = p[0].id
    all_commits = Commit.objects.filter(module_id=module_id)
    if request.method == 'POST':
        commit_form = CommitForm(request.POST, request.FILES, prefix="commit")
        if commit_form.is_valid():
            new_commit = Commit()
            new_commit.module_id = Module.objects.filter(id=module_id)[0]
            new_commit.name = commit_form.cleaned_data['name']
            new_commit.user_id = commit_form.cleaned_data['user_id']
            new_commit.description = commit_form.cleaned_data['description']
            new_commit.file = request.FILES['file']
            new_commit.publish = timezone.now()
            new_commit.save()
            return HttpResponseRedirect('/feed')

    else:
        commit_form = CommitForm
    context = {
        'all_commits': all_commits,
        'module': mod,
        'project_id': project_id,
        'commit_form':commit_form,
    }
    return render(request, 'feed/commit_detail.html', context)


def comment_detail(request, commit_id):
    commit = get_object_or_404(Commit, id=commit_id)
    all_comments = Comment.objects.filter(commit_id=commit)
    context = {
        'all_comments': all_comments,
    }
    return render(request, 'feed/comment_detail.html', context)


def test(request):
    return render(request, 'feed/test.html')
