from django.urls import path
from . import views

app_name = 'clienti'

urlpatterns = [
    path('creaCliente',views.ClienteCreate.as_view(), name='creaCliente'),
]
