# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1 style='text-align:center'>This is the feed for the best Intranet in the World.</h1>")