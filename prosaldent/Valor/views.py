from django.shortcuts import render, get_object_or_404
from .models import Opi, Valor

def Valor(request):
    Opis = Opi.objects.all()
    return render(request, "Valor/Valor.html", {'Opis':Opis})

def valoracion(request, valoracion_id):
    valoracion = get_object_or_404(valoracion, id=valoracion_id)
    return render(request, "Valor/valoracion.html", {'valoracion':valoracion})
