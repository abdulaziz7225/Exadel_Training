from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Notification


# Create your views here.
# Views for Notification model
class NotificationBaseView(View):
    model = Notification
    fields = '__all__'
    success_url = reverse_lazy('notification:all')


class NotificationListView(NotificationBaseView, ListView):
    """View to list all notifications
   Use the 'notification_list' variable in the template
   to access all Notification objects"""


class NotificationDetailView(NotificationBaseView, DetailView):
    """View to list the details from one notification.
    Use the 'notification' variable in the template to access
    the specific notification here and in the Views below"""


class NotificationCreateView(NotificationBaseView, CreateView):
    """View to create a new notification"""


class NotificationUpdateView(NotificationBaseView, UpdateView):
    """View to update a notification"""


class NotificationDeleteView(NotificationBaseView, DeleteView):
    """View to delete a notification"""
