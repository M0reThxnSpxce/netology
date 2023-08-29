import copy
from collections import OrderedDict

from rest_framework.settings import api_settings
from rest_framework.utils import model_meta


from rest_framework import serializers

# TODO: опишите необходимые сериализаторы


from .models import Sensor, Measurement

# Вариант 1
# class SensorSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()


# Вариант 2
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


