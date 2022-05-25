from unicodedata import name
from webbrowser import get
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from prosaldent.settings import EMAIL_HOST_USER 
from django.conf import settings

def contacto(request):
    return render(request, "Contacto.html")
def contactar(request):
    if request.method == "POST":
        asunto = request.POST.get("txtAsunto")
        mensaje = request.POST.get("txtMensaje")
        email = request.POST.get("txtEmail")
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["jhondeivyg2@gmail.com"]
        send_mail(asunto, mensaje, email, ["jhondeivygaravitocaicedo@gmail.com"], ["jhondeivyg2@gmail.com"])
        return render(request, "contactexi.html")
    return render(request, "Contacto.html")

   
    



    

