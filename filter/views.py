from django.shortcuts import render

def processTable(request):
    return render(request, 'filter/processTable.html')
