from django.contrib import admin
from .models import Contrato

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'medicos', 'tipo', 'possui_acordo', 'status', 'data_criacao')
    list_filter = ('possui_acordo', 'status')
    search_fields = ('contrato', 'medicos', 'tipo', 'observacao', 'email_principal', 'email_secundario')
