from django.urls import path
from measurement.views import SensorView, MeasurementCreateView, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('sensors/', sensors_met, name='sensors'),
    path('sensors/', SensorView.as_view(), name='sensors'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensordetail'),


]
