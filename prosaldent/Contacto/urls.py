from django.urls import path
from . import views
from Contacto.views import contacto,contactar

urlpatterns = [
    path('', views.contacto, name="Contacto"),
    path('', views.contactar, name="contactar"),
    path('Contacto/', contacto),
    path('contactar/', contactar),

]