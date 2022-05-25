from django.shortcuts import render

def Inicio(request):
    return render(request, "core/Inicio.html")

def Historia(request):
    return render(request, "core/Historia.html")

def Clientes(request):
    return render(request, "core/Clientes.html")

def Visita(request):
    return render(request, "core/Visita.html")

def Contacto(request):
    return render(request, "core/Contacto.html")

def Muestra(request):
    return render(request, "core/Muestra.html")