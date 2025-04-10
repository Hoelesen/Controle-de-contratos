from django.contrib import admin
from .models import Contrato, AuditLog

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    """
    Configurações do modelo Contrato no Django Admin.
    """
    list_display = ('contrato', 'medicos', 'tipo', 'possui_acordo', 'status', 'data_ativacao', 'data_inativacao', 'data_criacao')
    list_filter = ('possui_acordo', 'status')
    search_fields = ('contrato', 'medicos', 'tipo', 'observacao', 'email_principal', 'email_secundario')

    def save_model(self, request, obj, form, change):
        """
        Registra o usuário que fez a alteração no campo `modified_by`.
        """
        obj.modified_by = request.user  # Captura o usuário que fez a alteração
        super().save_model(request, obj, form, change)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    """
    Configurações do modelo AuditLog no Django Admin.
    """
    list_display = ('user', 'contrato', 'action', 'timestamp')
    list_filter = ('user', 'action')
    search_fields = ('user__username', 'contrato__contrato', 'action')
