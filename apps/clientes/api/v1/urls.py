from django.urls import path
from apps.clientes.api.v1.views.cliente import ClienteView

app_name = 'clientes'
urlpatterns = [
    #por defecto esta en get muestra
    path('lista-clientes/',ClienteView.as_view({'get':'list'}),name="cliente-list"),
    #para crear es po es metodo post
    path('crear-clientes/',ClienteView.as_view({'get':'create'}),name="cliente-crear"),
    #para Actializar
    path('editar-clientes/<int:id>',ClienteView.as_view({'get':'update'}),name="cliente-editar"),
    #para eliminar
    path('eliminar-clientes/<int:id>',ClienteView.as_view({'get':'delete'}),name="cliente-eliminar"),
    
]
