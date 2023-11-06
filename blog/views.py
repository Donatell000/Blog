from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет всем, это мой блог')
