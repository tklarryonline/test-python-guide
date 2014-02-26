from django.template.response import TemplateResponse
from django.views.generic.base import View


class IndexView(View):

    template = "polls/index.html"

    def get(self, request):
        context = {}
        context['var1'] = "This is Var 1"
        context['var2'] = ["This", "Is", "Var", "2", ]
        context['var3'] = {
            "part1": "This",
            "part2": "Is",
            "part3": "Var",
            "part4": "3",
        }

        return TemplateResponse(request, self.template, context)
