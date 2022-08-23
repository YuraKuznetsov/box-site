from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('calculations/index.html')
    return HttpResponse(template.render())


def valve_box(request):
    pass


def cutting_box(request):
    pass


def price(request):
    pass


def other(request):
    pass
