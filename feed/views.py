# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import ProjectForm, ModuleForm, CommitForm
from .models import Project, Module, Commit, Comment

# from django.template import loader

# Create your views here.
app_name = 'feed'


def index(request):
    all_projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = Project()
            new_project.name = form.cleaned_data['name']
            new_project.manager_id = form.cleaned_data['manager_id']
            new_project.description = form.cleaned_data['description']
            new_project.publish = timezone.now()
            new_project.save()
            return HttpResponseRedirect('/feed')

    else:
        form = ProjectForm()

    context = {'all_projects': all_projects,
               'form': form,
               'form_head': "Project",
               }
    return render(request, 'feed/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            new_module = Module()
            new_module.project_id = Project.objects.filter(id=project_id)[0]
            new_module.name = form.cleaned_data['name']
            new_module.description = form.cleaned_data['description']
            new_module.publish = timezone.now()
            new_module.save()
            return HttpResponseRedirect('/feed')

    else:
        form = ModuleForm

    return render(request, 'feed/detail.html', {'form': form,
                                                'form_head': "Module",
                                                'project':project,
                                              })


def commit_detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    p = Project.objects.filter(module=module)
    project_id = p[0].id
    all_commits = Commit.objects.filter(module_id=module_id)
    context = {
        'all_commits': all_commits,
        'module': module,
        'project_id': project_id,
    }
    return render(request, 'feed/commit_detail.html', context)


def comment_detail(request, commit_id):
    commit = get_object_or_404(Commit, id=commit_id)
    all_comments = Comment.objects.filter(commit_id=commit)
    context = {
        'all_comments': all_comments,
    }
    return render(request, 'feed/comment_detail.html', context)


def add_module(request, project_id):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            new_module = Module()
            new_module.project_id = Project.objects.filter(id=project_id)[0]
            new_module.name = form.cleaned_data['name']
            new_module.description = form.cleaned_data['description']
            new_module.publish = timezone.now()
            new_module.save()
            return HttpResponseRedirect('/feed')

    else:
        form = ModuleForm

    return render(request, 'feed/form.html', {'form': form,
                                              'form_head': "Module",
                                              })


def add_commit(request, module_id):
    if request.method == 'POST':
        form = CommitForm(request.POST, request.FILES)
        if form.is_valid():
            new_commit = Commit()
            new_commit.module_id = Module.objects.filter(id=module_id)[0]
            new_commit.name = form.cleaned_data['name']
            new_commit.user_id = form.cleaned_data['user_id']
            new_commit.description = form.cleaned_data['description']
            new_commit.file = request.FILES['file']
            new_commit.publish = timezone.now()
            new_commit.save()
            return HttpResponseRedirect('/feed')

    else:
        form = CommitForm

    return render(request, 'feed/form.html', {'form': form,
                                              'form_head': "Commit",
                                              })



# class FeedbackCreateView(AjaxCreateView):
#     form_class = FeedbackForm



# def ProjectUpdateView(request, UpdateView):
#     model = Project
#     form_class = ItemForm
#     template_name = 'feed/project_edit_form.html'
#
#     def dispatch(self, *args, *kwargs):
#         self.project_id = kwargs['pk']
#         return super(ProjectUpdateView, self).dispatch(*args, *kwargs)
#
#     def form_valid(self, form):
#         form.save()
#         project = Project.objects.get(id=self.project_id)
#         return render(request, 'feed/project_edit_form_success.html', {'project': project})
