
from django.utils import timezone
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from apps.clientes.models import Cliente
from apps.clientes.views.formulario import ClienteForm


from django.urls import reverse_lazy


class ClienteView(ListView):
    template_name = 'clientes/clientes.html'
    model = Cliente
    queryset = Cliente.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listarcarlos'] = timezone.now()
        return context
    
    
        
    
    
class CrearClienteViews(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name =  'clientes/form.html'
    success_url = reverse_lazy('clientes:cliente_list') 
    
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listarcarlos'] = timezone.now()
        return context    

class EditarClienteView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name =  'clientes/form.html'
    success_url = reverse_lazy('clientes:cliente_list')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listarcarlos'] = timezone.now()
        context['action'] = 'edit'
        return context 
    
class EliminaClienteView(DeleteView):
    model = Cliente
    
    template_name =  'clientes/eliminar.html'
    success_url = reverse_lazy('clientes:cliente_list') 
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listarcarlos'] = timezone.now()
        context['action'] = 'eliminar'
        return context 
     
     
     
     
    
""" class ClienteView(ListView,CreateView):
    
    ClienteForm = modelform_factory(request.POST)
    model = Cliente
    
         
    template_name = 'clientes/clientes.html'
    queryset = Cliente.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listarcarlos'] = timezone.now()
        return context
    
    
    def nuevoCliente(request):
        if request.method == 'POST':
            formcliente=ClienteForm(request.POST)
            if formcliente.is_valid():
                formcliente.save()
                return redirect('clientes/clientes.html')
            else:
                formcliente=ClienteForm()
                
            return render(request,'clientes/form.html')
             """
            
        
   
