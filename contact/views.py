from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    #print("Tipo de peticion:{}".format(request.method))
    #instancia
    contactForm=ContactForm()
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')

            email=EmailMessage(
                "La Cafettiera: Nuevo mensaje contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,message),
                "correo-prueba@inbox.mailtrap.io",
                ["lsanto@itsqmet.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except Exception as ex:
                print("Error: ", type(ex).__name__)

                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'contactForm':contactForm})


