from django.template.response import TemplateResponse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from polls.models import Question, Choice


class QuestionView(View):

    template = "polls/question.html"

    def get(self, request, question_id=None):
        context = {}
        context['question'] = get_object_or_404(Question, pk=question_id)
        return TemplateResponse(request, self.template, context)

    def post(self, request, question_id=None):
        choice = Choice.objects.get(pk=request.POST.get("poll_choice", None))
        choice.votes += 1
        choice.save()

        return HttpResponseRedirect(reverse("poll_result",
                                    kwargs={
                                        "question_id": choice.question_id
                                    }))
