# Django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# My imports
from .formulas import valveBox


def index(request):
    template = loader.get_template('calculations/home.html')
    return HttpResponse(template.render({}, request))


def valve_box(request):
    template = loader.get_template('calculations/valveBox.html')
    print('Прилетіло:', request.POST)
    print('Довжина:', len(request.POST))

    # Якщо заходити на чисту сторінку (без обрахунку)
    if len(request.POST) == 0:
        context = {
            'params': {
                'length': '', 'width': '', 'height': '',
                'layers': 'Т', 'marka': '21', 'profile': 'B', 'colour': 'brown', 'print': '0'
            },
            'price': '',
            'min_circulation': 3000,
        }
        return HttpResponse(template.render(context, request))

    context = {
        'params': request.POST,
        'price': 111,
        'min_circulation': 3000,
    }

    return HttpResponse(template.render(context, request))


def scotch(request):
    template = loader.get_template('calculations/scotch.html')
    return HttpResponse(template.render({}, request))

# def calc_valve_box(request):
#     # data = request.POST
#     data = request.GET
#     square = valveBox.get_square('B', int(data['length']), int(data['width']), int(data['height']))
#     # return HttpResponseRedirect(reverse('valveBox'))
#     return HttpResponse(f'{data},\n {square}')

