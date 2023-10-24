from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'), # Página inicial
    path('processos', views.processTable, name='processTable'), # Página de processos
]