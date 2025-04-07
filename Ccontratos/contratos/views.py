from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Contrato


def index(request):
    """
    View que exibe todos os contratos na página inicial.
    Permite acesso sem autenticação.
    """
    contratos = Contrato.objects.all()
    return render(request, 'contratos/index.html', {'contratos': contratos})


@login_required
def salvar_todos(request):
    """
    View que salva todos os checkboxes da página.
    Exige autenticação para funcionar.
    """
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("checado_"):
                contrato_id = key.split("_")[1]
                contrato = get_object_or_404(Contrato, id=contrato_id)
                contrato.checado = (value == "True")
                contrato.save()
        return redirect('contratos:index')
    return HttpResponse("Método não permitido", status=405)


def detalhes_contrato(request, id):
    """
    View que exibe os detalhes ou observações de um contrato.
    Funciona como resposta direta com base no tipo de requisição.
    """
    contrato = get_object_or_404(Contrato, id=id)
    tipo = request.GET.get("type")

    if tipo == "observacao":
        return HttpResponse(f"<p>Observação: {contrato.observacao}</p>")
    elif tipo == "detalhes":
        return HttpResponse(f"<p>Detalhes do Contrato ID: {id}</p>")
    else:
        return HttpResponse("<p>Erro: Tipo inválido!</p>")


@login_required
def atualizar_checado(request, id):
    """
    View que salva individualmente o estado de um checkbox.
    Exige autenticação para funcionar.
    """
    if request.method == "POST":
        contrato = get_object_or_404(Contrato, id=id)
        checado = request.POST.get("checado") == "True"  # Converte para boolean
        contrato.checado = checado
        contrato.save()
        return redirect('contratos:index')
    return HttpResponse("Método não permitido", status=405)
