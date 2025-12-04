from django.contrib import admin
from .models import Usuario, Endereco, Produto, Pedido, ItemPedido


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id_usuario", "nome", "email", "tipo")
    search_fields = ("nome", "email")
    list_filter = ("tipo",)


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("id_endereco", "rua", "numero", "bairro", "cidade", "usuario")
    search_fields = ("rua", "bairro", "cidade")
    list_filter = ("cidade", "bairro")


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id_produto", "nome", "preco", "estoque")
    search_fields = ("nome",)
    list_filter = ("preco",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id_pedido", "data_pedido", "status", "usuario", "endereco")
    search_fields = ("usuario__nome", "status")
    list_filter = ("status", "data_pedido")


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("id_item", "pedido", "produto", "quantidade", "preco_unit")
    search_fields = ("produto__nome",)
    list_filter = ("produto",)
