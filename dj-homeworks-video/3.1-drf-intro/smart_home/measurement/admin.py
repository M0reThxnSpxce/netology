from django.contrib import admin

# Register your models here.
import measurement.models
from measurement.models import *

class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 0
    verbose_name_plural = 'Датчик-Температура'

@admin.register(Sensor)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    inlines = [MeasurementInline, ]


@admin.register(Measurement)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'created_at']
