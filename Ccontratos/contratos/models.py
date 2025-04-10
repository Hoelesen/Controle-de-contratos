from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contrato(models.Model):
    contrato = models.IntegerField(verbose_name="Contrato", default=0)
    medicos = models.CharField(max_length=255, verbose_name="Médicos")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    possui_acordo = models.BooleanField(default=False, verbose_name="Possui Acordo")
    observacao = models.TextField(verbose_name="Observação")
    email_principal = models.EmailField(verbose_name="Email Principal")
    email_secundario = models.EmailField(blank=True, null=True, verbose_name="Email Secundário")
    status = models.CharField(max_length=50, verbose_name="Status")
    data_ativacao = models.DateField(null=True, blank=True)
    data_inativacao = models.DateField(null=True, blank=True)
    checado = models.BooleanField(default=False, verbose_name="Checado")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Modificado por")

    def __str__(self):
        return f"Contrato {self.contrato} - {self.status}"

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} em {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}"
