from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Inicio, name="Inicio"),
    path('Historia/', views.Historia, name="Historia"),
    path('Visita/', views.Visita, name="Visita"),
    
    

]