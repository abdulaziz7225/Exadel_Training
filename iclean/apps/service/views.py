from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse

# Create your views here.
def index(request, text):
    try:
        return render(request, "service/index.html")
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()

def say_hello(request):
    return HttpResponse("Hello World from apps.service")
