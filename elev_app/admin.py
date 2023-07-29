from django.contrib import admin
from .models import ElevatorModel, RequestModel


admin.site.register(ElevatorModel)
admin.site.register(RequestModel)