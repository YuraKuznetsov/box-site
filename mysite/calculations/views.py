# Django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Prices20, Prices30              # Db import
from .valveBox import Box                           # My imports


def index(request):
    template = loader.get_template('calculations/home.html')
    return HttpResponse(template.render({}, request))


def valve_box(request):
    # Сторінка
    template = loader.get_template('calculations/valveBox.html')

    # Якщо заходити на чисту сторінку (без обрахунку)
    if len(request.POST) == 0:
        context = {
            'params': {
                'length': '', 'width': '', 'height': '',
                'layers': 'Т', 'marka': '21', 'profile': 'B', 'colour': 'brown', 'printing': '0'
            },
            'price': '-',
            'square': '-',
            'min_circulation': '-',
        }
        return HttpResponse(template.render(context, request))

    # Клас коробки
    MyBox = Box(request.POST)

    context = {
        'params': request.POST,
        'price': MyBox.get_price(),
        'square': MyBox.get_square(),
        'min_circulation': 3000,
    }

    return HttpResponse(template.render(context, request))


def scotch(request):
    template = loader.get_template('calculations/scotch.html')
    return HttpResponse(template.render({}, request))


def prices(request):
    template = loader.get_template('calculations/prices.html')
    return HttpResponse(template.render({}, request))


def prices20(request):
    template = loader.get_template('calculations/prices20.html')

    # Обробка інфи з бази для зручного використання в html
    data = {}
    for mark in range(20, 27):
        for profile in ('E', 'B', 'C'):
            for color in ('white', 'brown'):
                data[f'{mark}_{profile}_{color}'] = Prices20.objects.get(mark=mark, profile=profile, color=color).price

    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))


def save20(request):
    print(request.POST, "----------------------------------------------------------")
    # Перебираємо усі можливі параметри
    for mark in range(20, 27):
        for profile in ('E', 'B', 'C'):
            for color in ('white', 'brown'):

                # Змінюємо ціни у базі даних
                item = Prices20.objects.get(mark=mark, profile=profile, color=color)
                item.price = request.POST[f'{mark}_{profile}_{color}']
                item.save()

    return HttpResponseRedirect(reverse('prices'))


def prices30(request):
    template = loader.get_template('calculations/prices30.html')

    data30 = {}
    for mark in range(30, 35):
        for profile in ('EB', 'EC', 'BC'):
            for color in ('white', 'brown'):
                data30[f'{mark}_{profile}_{color}'] = Prices30.objects.get(mark=mark, profile=profile, color=color).price

    print(data30)

    context = {
        'marks': ('30', '31', '32', '33', '34'),
        'profiles': ('EB', 'EC', 'BC'),
        'colors': ('brown', 'white'),
        'data': data30,
    }
    return HttpResponse(template.render(context, request))


def save30(request):
    print(request.POST, "----------------------------------------------------------")

    for mark in range(30, 35):
        for profile in ('EB', 'EC', 'BC'):
            for color in ('white', 'brown'):
                # Prices30(mark=mark, profile=profile, color=color, price=0).save()

                # Змінюємо ціни у базі даних
                item = Prices30.objects.get(mark=mark, profile=profile, color=color)
                item.price = request.POST[f'{mark}_{profile}_{color}']
                item.save()

    return HttpResponseRedirect(reverse('prices'))
