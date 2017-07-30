# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

#Project Table -- contains info for a particular project.

class Projects(models.Model):
    name = models.CharField(max_length=250)
    manager_id = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    publish = models.DateField()
    terminate = models.DateField(null=True)
    def __str__(self):
        return self.name + ' - ' + self.description


#Module Table -- Contains info of all the modules from all the projects, and can be grouped into
#a particular project using the project id

class Modules(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    publish = models.DateTimeField()
    terminate = models.DateTimeField(null=True)



#Commit Table -- Contains all the information of all the commits till date for all the modules of
#all the projects. They can be grouped together using the module_id

class Commits(models.Model):
    module_id = models.ForeignKey(Modules, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    description = models.CharField(max_length=1000)
    publish = models.DateTimeField()
    file = models.CharField(max_length=1000,null=True)

#Comments Table -- Contains all the comments till date. They can be grouped together using the
#commit_id. Whenever a client reads a commit he may post a comment and that comment can then
#be retrieved using the commit_id

class Comments(models.Model):
    commit_id = models.ForeignKey(Commits,on_delete=models.CASCADE)
    user_id = models.IntegerField()
    description = models.CharField(max_length=1000)
    publish = models.DateTimeField()
    file = models.CharField(max_length=1000,null=True)


#Log Table -- It will contain the log entry of every individual working in the organisation.
#Whenever the user asks to logout he will be prompted to enter the summary of the work he has done
#on that day.

class Summary(models.Model):
    user_id = models.IntegerField()
    description = models.CharField(max_length=1000)
    publish = models.DateTimeField()