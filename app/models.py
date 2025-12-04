from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=120)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100, null=True, blank=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rua}, {self.numero}"


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido #{self.id_pedido}"


class ItemPedido(models.Model):
    id_item = models.AutoField(primary_key=True)
    quantidade = models.IntegerField()
    preco_unit = models.DecimalField(max_digits=10, decimal_places=2)

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"