from django.contrib import admin
from .models import Service, ServiceType

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceType)
