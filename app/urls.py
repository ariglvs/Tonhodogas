from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.produtos, name="produtos"),
    path("criar-usuario/", views.criar_usuario, name="criar_usuario"),
]