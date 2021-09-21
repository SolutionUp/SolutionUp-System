from django.db import models
from produtos.models import Contato, Produto
     
class Clientes(Contato):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Pedido(models.Model):
    STATUS_CHOICES = (
        ("E", "Enviado"),
        ("R", "Realizado"),
	    ("F", "Finalizado"),
	    ("C", "Cancelado"),
    )
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rastreio = models.CharField(max_length=30, blank=False, null=False)
    comprovante = models.ImageField(null=True, blank=True)
    taxa_entrega = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, blank=False, null=False)
   
    cliente = models.ForeignKey(Clientes, related_name='pedido_cliente', null=False, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produto, related_name='pedido_produto', null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id} - {self.cliente}'
