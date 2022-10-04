from rest_framework.response import Response
#from rest_framework.generics import ListAPIView
from apps.clientes.models import Cliente
from apps.contrib.api.viewsets import ModelCreateListViewSet
from rest_framework import viewsets

import json

from rest_framework import status

from apps.clientes.api.v1.serializers.clienteSerial import ClienteSerializer2

class ClienteView(ModelCreateListViewSet):
    model= Cliente
    serializer_class = ClienteSerializer2
    queryset = Cliente.objects.all()
    
    def list(self, request, *arg, **kwargs):
        print("ingrsanado al metofo de Alex")
        clientes = Cliente.objects.all()
        cliente_serializer=ClienteSerializer2(clientes,many=True)
        print("Clientes Consulta\n",clientes)
        print("\nClientes Serializer\n",cliente_serializer)
        return self.get_paginated_response(self.paginate_queryset(cliente_serializer.data))
        
    
    #para crear
    def create(self, request, *args, **kwarga):
        #este metodo es para crear un registro nuevo de un cliente
        print("Creando un nuevo Cliente")
        #datosJSON = json.loads(request.body)
        crearCliene=Cliente.objects.create(nombres='carlitos',apellidos='mamani',numero_identidad='123456')
        cliente_serializer=ClienteSerializer2(crearCliene,many=True)
        return Response({'mensaje':'cliente creado'})
    
    #para actualizar
    def update(self, request, id):
        #este metodo es para acrualizar un cliente
        print("acutalizando un  Cliente")
        actualizarCliene=list(Cliente.objects.filter(id=id).values())
        cliente_serializer=ClienteSerializer2(actualizarCliene,many=True)
        if id>0:
            updateClientes=Cliente.objects.get(id=id)
            updateClientes.nombres='editado'
            updateClientes.apellidos='editado'
            updateClientes.numero_identidad='editado'
            updateClientes.save()
            datos={"mensaje":"cliente actualizado"}
        else:
            datos={"mensaje":" NO se a actualizado el cliente"}

        return Response(datos  )
    
        #para delete
    def delete(self, request, id):
        #este metodo es para acrualizar un cliente
        print("eliminando un  Cliente")
        eliminarCliene=list(Cliente.objects.filter(id=id).values())
        cliente_serializer=ClienteSerializer2(eliminarCliene,many=True)
        if id>0:
            eliminarCliene=Cliente.objects.filter(id=id).delete()
            
            datos={"mensaje":"se elimino el registro"}
        else:
            datos={"mensaje":" NO se a eliminado el registro"}

        return Response(datos  )
    
    
    