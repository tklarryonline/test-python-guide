from django.conf.urls import patterns, include, url
from polls.views.index_view import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
)
