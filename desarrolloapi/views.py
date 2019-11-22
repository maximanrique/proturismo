from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def galeria(request):
    return render(request,"galeria.html")

def contacto(request):
    return render(request,"contacto.html")