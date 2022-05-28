from django.contrib import admin
from .models import Request, Request_status
# Register your models here.

admin.site.register(Request)
admin.site.register(Request_status)
