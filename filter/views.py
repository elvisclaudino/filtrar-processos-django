from django.shortcuts import render
from django.db import connection

from .models import Processos, Pessoas
from django.db.models import Subquery, OuterRef

def processTable(request):
    processos = Processos.objects.all()

    return render(request, 'filter/processTable.html', {'processos': processos})
