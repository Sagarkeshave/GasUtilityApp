from django.contrib import admin
from .models import ServiceRequest, SupportRepresentative
# Register your models here.

admin.site.register(ServiceRequest)
admin.site.register(SupportRepresentative)