#la url de afuera es para centralizar todas la urls

from django.urls import path, include

app_name = 'clientes'
urlpatterns = [
    path('v1/', include('apps.clientes.api.v1.urls', namespace='v1')),
]
