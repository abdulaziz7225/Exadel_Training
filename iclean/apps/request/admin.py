from django.contrib import admin
from .models import Request, RequestStatus
# Register your models here.

admin.site.register(Request)
admin.site.register(RequestStatus)
