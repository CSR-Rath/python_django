from django.http import HttpResponse


def startup(request):
    return HttpResponse("Hello world!")
