from django.urls import path

from . import views

urlpatterns = [
    path('', views.processTable, name='processTable'),
]