from rest_framework import serializers
from .models import ElevatorModel, RequestModel


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorModel
        fields = '__all__'



class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'