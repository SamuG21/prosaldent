from django.shortcuts import render

def Clientes(request):
    return render(request, "Clientes/Clientes.html", {'Clientes':Clientes})
