from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.utils import timezone

from polls.models import Question


class IndexView(View):

    template = "polls/index.html"

    def get(self, request):
        context = {}
        """
        Returns the recent 5 questions published, not including those set
        to be in the future
        """
        context['questions'] = Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]
        context['today_questions'] = Question.objects.published_recently().order_by("-pub_date")[:5]

        return TemplateResponse(request, self.template, context)
