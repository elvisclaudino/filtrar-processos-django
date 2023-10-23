from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=128)
    cliente = models.IntegerField()
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereço = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas'

    def __str__(self):
        return self.nome


class Processos(models.Model):
    advogado_id = models.IntegerField()
    cliente_id = models.IntegerField()
    numero_processo = models.CharField(max_length=35)
    proximo_prazo = models.DateTimeField()
    arquivo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'processos'

    def __str__(self):
        return self.numero_processo
