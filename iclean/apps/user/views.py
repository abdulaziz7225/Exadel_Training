from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.

def index(request):
    try:
        return render(request, "user/index.html")
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


def say_hello(request):
    return HttpResponse("Hello World from apps.user")


def register(request):
    data = request.data
    return HttpResponse("Hello World from apps.user")
