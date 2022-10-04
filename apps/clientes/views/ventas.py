
from apps.clientes.models.ventas import Ventas
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.utils import timezone


class VenteasView(ListView):
    template_name = 'clientes/listaVentas.html'
    model = Ventas
    queryset = Ventas.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ventaslista'] = timezone.now()
        return context
    
    
        