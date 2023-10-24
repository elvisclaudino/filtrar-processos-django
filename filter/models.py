from django.db import models

class Pessoas(models.Model): 
    nome = models.CharField(max_length=128) 
    cliente = models.BooleanField() 
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereço = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas'

    def __str__(self):
        return self.nome


class Processos(models.Model):
    advogado = models.ForeignKey(Pessoas, on_delete=models.DO_NOTHING, related_name='advogado_processos', db_column='advogado_id') 
    cliente = models.ForeignKey(Pessoas, on_delete=models.DO_NOTHING, related_name='cliente_processos', db_column='cliente_id')
    numero_processo = models.CharField(max_length=35)
    proximo_prazo = models.DateTimeField()
    arquivo = models.BooleanField()


    class Meta:
        managed = False
        db_table = 'processos'

    def __str__(self):
        return self.numero_processo
