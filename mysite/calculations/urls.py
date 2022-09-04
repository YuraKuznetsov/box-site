from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('valveBox/', views.valve_box, name='valveBox'),
    path('scotch/', views.scotch, name='scotch'),
    # path('valveBox/calcValveBox/', views.calc_valve_box, name='calcValveBox'),
]