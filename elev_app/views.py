from django.shortcuts import render
from rest_framework import viewsets
from .models import ElevatorModel, RequestModel
from .serializers import ElevatorSerializer, RequestSerializer
from . logic import ElevatorSystem


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = ElevatorModel.objects.all()
    serializer_class = ElevatorSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer


