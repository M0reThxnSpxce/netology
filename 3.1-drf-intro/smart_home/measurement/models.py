from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
