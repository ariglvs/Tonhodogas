from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Endereco, Produto, Pedido, ItemPedido

def require_login(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("usuario_id"):
            return redirect("login")
        return view_func(request, *args, **kwargs)
    return wrapper

@require_login
def home(request):
    if "usuario_id" not in request.session:
        return redirect("login")

    usuario = Usuario.objects.get(pk=request.session["usuario_id"])
    return render(request, "home.html", {"usuario": usuario})

@require_login
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})

@require_login
def criar_produto(request):
    if request.method == "POST":
        Produto.objects.create(
            nome=request.POST["nome"],
            preco=request.POST["preco"],
            descricao=request.POST["descricao"],
            estoque=request.POST["estoque"]
        )
        return redirect("produtos")

    return render(request, "criar_produto.html")

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

@require_login
def criar_endereco(request):
    
    usuarios = Usuario.objects.all().order_by("nome")

    if request.method == "POST":
        
        usuario_id = request.POST.get("usuario")
        rua = request.POST.get("rua", "").strip()
        numero = request.POST.get("numero", "").strip()
        bairro = request.POST.get("bairro", "").strip()
        cidade = request.POST.get("cidade", "").strip()
        complemento = request.POST.get("complemento", "").strip()

        
        if not usuario_id or not rua or not numero or not bairro or not cidade:
            msg = "Preencha todos os campos obrigatórios."
            return render(request, "criar_endereco.html", {"usuarios": usuarios, "erro": msg})

        usuario = get_object_or_404(Usuario, pk=usuario_id)

        
        Endereco.objects.create(
            rua=rua,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            complemento=complemento,
            usuario=usuario
        )

        return redirect("home")

    
    return render(request, "criar_endereco.html", {"usuarios": usuarios})

@require_login
def pedidos(request):
    lista = Pedido.objects.all()
    return render(request, "pedidos.html", {"pedidos": lista})

@require_login
def criar_pedido(request):
    usuarios = Usuario.objects.all()
    enderecos = Endereco.objects.all()
    produtos = Produto.objects.all()

    if request.method == "POST":
        usuario_id = request.POST["usuario"]
        endereco_id = request.POST["endereco"]
        produto_id = request.POST["produto"]
        quantidade = int(request.POST["quantidade"])

        usuario = get_object_or_404(Usuario, pk=usuario_id)
        endereco = get_object_or_404(Endereco, pk=endereco_id)
        produto = get_object_or_404(Produto, pk=produto_id)

        pedido = Pedido.objects.create(
            usuario=usuario,
            endereco=endereco,
            status="Aguardando"
        )

        ItemPedido.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=quantidade,
            preco_unit=produto.preco
        )

        return redirect("pedidos")

    return render(request, "criar_pedido.html", {
        "usuarios": usuarios,
        "enderecos": enderecos,
        "produtos": produtos
    })

def login(request):
    erro = ""

    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]

        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            request.session["usuario_id"] = usuario.id_usuario
            request.session["usuario_nome"] = usuario.nome
            return redirect("home")
        except Usuario.DoesNotExist:
            erro = "Email ou senha incorretos."

    return render(request, "login.html", {"erro": erro})

def logout(request):
    request.session.flush()
    return redirect("login")
