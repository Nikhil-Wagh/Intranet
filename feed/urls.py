from django.conf.urls import url

from . import views

app_name = 'feed'

urlpatterns = [
    # /feed/
    url(r'^$', views.index, name='index'),

    # /feed/34<project_id>
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),

    # /feed/<project_id>/<module_id>
    url(r'^([0-9]+)/(?P<module_id>[0-9]+)/$', views.commit_detail, name = 'commit_detail')
    
]