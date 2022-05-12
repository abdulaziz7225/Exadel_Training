from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review


# Create your views here.
# Views for Notification model
class ReviewBaseView(View):
    model = Review
    fields = '__all__'
    success_url = reverse_lazy('review:all')


class ReviewListView(ReviewBaseView, ListView):
    """View to list all notifications
   Use the 'notification_list' variable in the template
   to access all Notification objects"""


class ReviewDetailView(ReviewBaseView, DetailView):
    """View to list the details from one notification.
    Use the 'notification' variable in the template to access
    the specific notification here and in the Views below"""


class ReviewCreateView(ReviewBaseView, CreateView):
    """View to create a new notification"""


class ReviewUpdateView(ReviewBaseView, UpdateView):
    """View to update a notification"""


class ReviewDeleteView(ReviewBaseView, DeleteView):
    """View to delete a notification"""
