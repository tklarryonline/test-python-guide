from django.conf.urls import patterns, url
from polls.views.index_view import IndexView
from polls.views.question_view import QuestionView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^(?P<question_id>\d+)$', QuestionView.as_view(), name="poll_detail"),
    url(r'^(?P<question_id>\d+)/result$', QuestionView.as_view(template="polls/result.html"), name="poll_result"),
)
