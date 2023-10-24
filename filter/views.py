from django.shortcuts import render
from django.core.paginator import Paginator
from django.db import connection
from django.http import HttpResponse

from .models import Processos

def processTable(request):
    lista_processos = Processos.objects.all().order_by("id")
    paginator = Paginator(lista_processos, 10)
    page = request.GET.get("page")
    processos = paginator.get_page(page)

    return render(request, 'filter/processTable.html', {'processos': processos})
