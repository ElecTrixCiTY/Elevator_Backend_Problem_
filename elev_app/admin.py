from django.contrib import admin
from .models import ElevatorModel, ElevatorSystemModel


admin.site.register(ElevatorModel)
admin.site.register(ElevatorSystemModel)