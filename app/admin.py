from django.contrib import admin
from .models import Usuario, Endereco, Produto, Pedido, ItemPedido

admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
