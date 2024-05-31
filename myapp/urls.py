from django.urls import path
from .simulacion_view import *

urlpatterns = [
    path('siguiente/', siguiente_paso, name='siguiente paso'),
    path('reiniciar/', reiniciar_simulacion, name='reiniciar'),
    path('fuego/', pender_fuego, name='prender fuego'),
    path('agua/', poner_agua, name='poner agua'),
    path('viento/', cambiar_viento, name='cambiar viento'),
]
