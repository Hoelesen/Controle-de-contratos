from django.db import models

class Contrato(models.Model):
    contrato = models.IntegerField(verbose_name="Contrato", default=0)
    medicos = models.CharField(max_length=255, verbose_name="Médicos")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    possui_acordo = models.BooleanField(default=False, verbose_name="Possui Acordo")
    observacao = models.TextField(verbose_name="Observação")
    email_principal = models.EmailField(verbose_name="Email Principal")
    email_secundario = models.EmailField(blank=True, null=True, verbose_name="Email Secundário")
    status = models.CharField(max_length=50, verbose_name="Status")
    checado = models.BooleanField(default=False, verbose_name="Checado")  # Novo campo
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"Contrato {self.contrato} - {self.status}"

