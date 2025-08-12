from django.shortcuts import render # type: ignore

# Create your views here.
def  index(request):
    return render(request,"index.html")

def cadastro(request):
    return render(request, "cadastro.html")

def produtos(request):
    return render(request, "produtos.html")

def endereco(request):
    return render(request, "endereco.html")

def pagamento(request):
    return render(request, "pagamento.html")

