# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Project, Module, Comment, Commit

# Register your models here.

admin.site.register(Project)
admin.site.register(Module)
admin.site.register(Comment)
admin.site.register(Commit)