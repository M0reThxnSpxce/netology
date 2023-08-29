# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# @api_view(['GET'])
# def sensors_met(request):
#     if request.method == 'GET':
#         sensor_objects = Sensor.objects.all()
#         # serializer = [{'id': i.id, 'name': i.name, 'description': i.description} for i in sensor_objects]
#         serializer = SensorSerializer(sensor_objects, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         return Response({'Status': 'OK'})

#
# class SensorView(APIView):
#     def get(self, request):
#         sensor_objects = Sensor.objects.all()
#         serializer = SensorSerializer(sensor_objects, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         return Response({'Status': 'OK'})


# 1, 4
class SensorView(ListCreateAPIView):
    """Список датчиков / Добавить датчик"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 2, 5
class SensorDetailView(RetrieveUpdateAPIView):
    """Получить данные по датчику / Изменить данные по датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# 3
class MeasurementCreateView(CreateAPIView):
    """Добавить температуру"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):

        try:
            sen = Sensor.objects.get(id=request.data.get('sensor'))

            match request.data:
                case {**kwargs} if len(kwargs) != 2 or 'temperature' not in kwargs:
                    return Response({'Ошибка запроса': 'Необходимо передать строго 2 ключа (sensor и temperature)'})
                case {'sensor': int(sen.id), 'temperature': int() | float() as tem}:
                    Measurement.objects.create(sensor_id=sen.id, temperature=tem)
                    return Response({'sensor': sen.id, 'temperature': tem})

        except ObjectDoesNotExist:
            return Response({'Ошибка запроса': 'Датчик не указан или отсутствует в БД'})
