from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Привет всем, это мой блог')
