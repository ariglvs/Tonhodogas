# app/urls.py (adicione a linha)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.produtos, name="produtos"),
    path("criar-produto/", views.criar_produto, name="criar_produto"),
    path("criar-usuario/", views.criar_usuario, name="criar_usuario"),
    path("criar-endereco/", views.criar_endereco, name="criar_endereco"),  # <--- nova rota
    path("pedidos/", views.pedidos, name="pedidos"),
    path("criar-pedido/", views.criar_pedido, name="criar_pedido"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]