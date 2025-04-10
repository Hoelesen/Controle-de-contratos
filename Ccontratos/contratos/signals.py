from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AuditLog, Contrato

@receiver(post_save, sender=Contrato)
def log_alteracoes(sender, instance, created, **kwargs):
    AuditLog.objects.create(
        user=instance.modified_by,  # Certifique-se de que isso está sendo capturado
        contrato=instance,
        action="Criado" if created else "Alterado"
    )
