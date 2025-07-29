from django.shortcuts import render # type: ignore

# Create your views here.
def  index(request):
    return render(request,"index.html")

def cadastro(request):
    return render(request, "cadastro.html")