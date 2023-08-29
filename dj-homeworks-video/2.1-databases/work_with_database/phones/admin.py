from django.contrib import admin

# Register your models here.
from phones.models import *

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date']
    list_editable = ['name', 'price', ]

