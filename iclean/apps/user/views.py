from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import User


# Create your views here.
# Views for User model
class UserBaseView(View):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('user:all')


class UserListView(UserBaseView, ListView):
    """View to list all users.
   Use the 'user_list' variable in the template
   to access all User objects"""


class UserDetailView(UserBaseView, DetailView):
    """View to list the details from one user.
    Use the 'user' variable in the template to access
    the specific user here and in the Views below"""


class UserCreateView(UserBaseView, CreateView):
    """View to create a new user"""


class UserUpdateView(UserBaseView, UpdateView):
    """View to update a user"""


class UserDeleteView(UserBaseView, DeleteView):
    """View to delete a user"""

