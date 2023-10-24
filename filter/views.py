from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Processos # Importa o modelo de processos

def home(request):
    return render(request, 'filter/home.html') # Renderiza a página inicial

def processTable(request):
    lista_processos = Processos.objects.all().order_by("proximo_prazo") # Salava todos os processos em uma lista e ordena por id
    paginator = Paginator(lista_processos, 10) # Mostra apenas 10 processos por página
    page = request.GET.get("page") # Pega o número da página
    processos = paginator.get_page(page) # Pega os processos da página

    return render(request, 'filter/processTable.html', {'processos': processos}) # Renderiza a página com os processos
