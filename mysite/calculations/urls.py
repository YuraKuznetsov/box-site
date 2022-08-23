from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('valveBox', views.index, name='valveBox'),
    path('cuttingBox', views.index, name='cuttingBox'),
    path('price', views.index, name='price'),
    path('other', views.index, name='other'),
]