from django.shortcuts import render, redirect
from .models import Produto, Pedido, Usuario

def home(request):
    return render(request, "home.html")

def produtos(request):
    lista = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": lista})

def criar_usuario(request):
    if request.method == "POST":
        Usuario.objects.create(
            nome=request.POST["nome"],
            email=request.POST["email"],
            senha=request.POST["senha"],
            tipo=request.POST["tipo"]
        )
        return redirect("home")
    return render(request, "criar_usuario.html")
