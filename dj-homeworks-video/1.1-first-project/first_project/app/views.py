from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.conf import settings
import time
import os


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages,
        'title': 'Главная страница'
    }
    return render(request, template_name, context=context)


def time_view(request):
    current_time = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)



def workdir_view(request):
    rez = ' | '.join(os.listdir(settings.BASE_DIR))

    return HttpResponse(rez)
