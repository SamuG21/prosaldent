from django.urls import path
from . import views

urlpatterns = [
    path('', views.Valor, name="Valor"),
    path('valoracion/<int:valoracion_id>/', views.valoracion, name="valoracion"),
]