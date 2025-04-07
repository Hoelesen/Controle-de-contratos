from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contratos.urls')),  # Inclui as URLs do aplicativo `contratos`
]
