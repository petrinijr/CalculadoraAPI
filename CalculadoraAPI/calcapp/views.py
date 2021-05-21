from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Test


class ViewTests(View):
    tests_names = Test.objects.values_list("name", flat=True)

    tests_str = "<br>".join(tests_names)

    output = f"The following tests have been peformed so far:<br>{tests_str}"

    def get(self, request):
        return HttpResponse(self.output)


def corinthians(request):
    return HttpResponse('Vai Corinthians')
