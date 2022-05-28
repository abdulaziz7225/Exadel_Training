from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Request


# Create your views here.
# Views for Notification model
class RequestBaseView(View):
    model = Request
    fields = '__all__'
    success_url = reverse_lazy('request:all')


class RequestListView(RequestBaseView, ListView):
    """View to list all notifications
   Use the 'notification_list' variable in the template
   to access all Notification objects"""


class RequestDetailView(RequestBaseView, DetailView):
    """View to list the details from one notification.
    Use the 'notification' variable in the template to access
    the specific notification here and in the Views below"""


class RequestCreateView(RequestBaseView, CreateView):
    """View to create a new notification"""


class RequestUpdateView(RequestBaseView, UpdateView):
    """View to update a notification"""


class RequestDeleteView(RequestBaseView, DeleteView):
    """View to delete a notification"""
