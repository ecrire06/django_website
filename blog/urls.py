"""
URL pattern is composed of a Python regular expression
Take a look at
https://docs.python.org/3/howto/regex.html
"""

from blog.feeds import LatestPostsFeed
from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'blog'

urlpatterns = [
    # This is a previous version of writing an urlpatterns (using regular expression)
#    url(r'^$', views.post_list, name='post_list'),
#    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
#        r'(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),

    # This is a new version of writing an urlpatterns [django ver 2.0 and after]
#     post views
#        Check views.py in blog directory
#        I. if you want to use "def post_list(request)"
#            set path('', views.post_list ~)
#        II. if you want to use "class PostListView(ListView)"
#            set path('', views.PostListView.as_view() ~)
    path('', views.post_list, name='post_list'),
#    path('', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    path('feed', LatestPostsFeed(), name='post_feed'),
]