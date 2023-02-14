from django.shortcuts import render
from .models import Valor


def index(request, value):
    valor = Valor(num=value)
    valor.save()
    return render(request, 'index.html')