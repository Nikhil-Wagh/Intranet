from django.conf.urls import url

from . import views

urlpatterns = [
    # /feed/
    url(r'^$', views.index, name='index'),

    # /feed/34(Project ID)
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
]