from django.shortcuts import render, HttpResponse

# Create your views here.

"""
Inicio - home/
Historia - about/
Servicios - services/
Visitanos - store/
Contacto - contact/
Blog - blog/
Samples - sample


"""
def  home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")



def store(request):
    return render (request, "core/store.html")




