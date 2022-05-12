from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Service


# Create your views here.
# Views for Notification model
class ServiceBaseView(View):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service:all')


class ServiceListView(ServiceBaseView, ListView):
    """View to list all notifications
   Use the 'notification_list' variable in the template
   to access all Notification objects"""


class ServiceDetailView(ServiceBaseView, DetailView):
    """View to list the details from one notification.
    Use the 'notification' variable in the template to access
    the specific notification here and in the Views below"""


class ServiceCreateView(ServiceBaseView, CreateView):
    """View to create a new notification"""


class ServiceUpdateView(ServiceBaseView, UpdateView):
    """View to update a notification"""


class ServiceDeleteView(ServiceBaseView, DeleteView):
    """View to delete a notification"""
