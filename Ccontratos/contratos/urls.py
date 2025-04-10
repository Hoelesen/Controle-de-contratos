from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'contratos'

urlpatterns = [
    path('', views.index, name='index'),  # Página principal com o nome 'index'
    path('detalhes/<int:id>/', views.detalhes_contrato, name='detalhes'),
    path('atualizar_checado/<int:id>/', views.atualizar_checado, name='atualizar_checado'),
    path('salvar_todos/', views.salvar_todos, name='salvar_todos'),
    path('auditoria/', views.auditoria_filtrada, name='auditoria_filtrada'),  # Adicionando auditoria filtrada
    path('login/', LoginView.as_view(template_name='contratos/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
