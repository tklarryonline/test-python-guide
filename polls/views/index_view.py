from django.template.response import TemplateResponse
from django.views.generic.base import View

from polls.models import Question


class IndexView(View):

    template = "polls/index.html"

    def get(self, request):
        context = {}
        context['questions'] = Question.objects.all()

        return TemplateResponse(request, self.template, context)
