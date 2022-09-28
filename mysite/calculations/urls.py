from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('valveBox/', views.valve_box, name='valveBox'),
    # path('valveBox/calcValveBox/', views.calc_valve_box, name='calcValveBox'),
    path('scotch/', views.scotch, name='scotch'),
    path('prices/', views.prices, name='prices'),
    path('prices/20/', views.prices20, name='prices20'),
    path('prices/20/save', views.save20, name='save20'),
    path('prices/30/', views.prices30, name='prices30'),
    path('prices/30/save', views.save30, name='save30'),
]
