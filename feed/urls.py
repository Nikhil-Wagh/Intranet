from django.conf.urls import url

from . import views

# from feed.views import FeedbackCreateView

app_name = 'feed'

urlpatterns = [
    # /feed/
    url(r'^$', views.index, name='index'),

    # /feed/34<project_id>
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),

    # /feed/<project_id>/<module_id>
    url(r'^([0-9]+)/(?P<module_id>[0-9]+)/$', views.commit_detail, name='commit_detail'),

    url(r'^test/', views.test, name="test"),
    # # /feed/<project_id>/<module_id>/<commit_id>
    # url(r'^([0-9]+)/(?P<module_id>[0-9]+)/add/$', views.add_commit, name='add_commit'),
    url(r'^([0-9]+)/([0-9]+)/(?P<commit_id>[0-9]+)/$', views.comment_detail, name='comment_detail'),

    # url(r'^create/$', FeedbackCreateView.as_view(), name="feedback_create"),
]
