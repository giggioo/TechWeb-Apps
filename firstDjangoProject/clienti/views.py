from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from clienti.models import Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ('nome', 'cognome', 'telefono')
    template_name = 'creaCliente.html'
    success_url = reverse_lazy('clienti:listaClienti')
    

