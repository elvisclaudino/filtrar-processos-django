from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Processos # Importa o modelo de processos

def processTable(request):
    search = request.GET.get("search") # Pega o valor da busca
    lista_processos = [] # Lista vazia para armazenar os processos

    if search: # Se houver uma busca
        try:
            search_id = int(search) # Tenta converter o valor de search para inteiro
            lista_processos = Processos.objects.filter(advogado_id=search_id) # Salva todos os processos em uma lista

        except ValueError:
            processos = Processos.objects.none() # Caso não seja um inteiro, retorna uma lista vazia

    else: # Caso não haja busca
        lista_processos = Processos.objects.all().order_by("proximo_prazo") # Salva todos os processos em uma lista e ordena por id

    paginator = Paginator(lista_processos, 10) # Mostra apenas 10 processos por página
    page = request.GET.get("page") # Pega o número da página
    processos = paginator.get_page(page) # Pega os processos da página

    return render(request, 'filter/processTable.html', {'processos': processos, 'search': search}) # Renderiza a página com os processos
