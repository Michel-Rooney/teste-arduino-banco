from django.shortcuts import render, HttpResponse
from .models import Valor


def index(request, value):
    valor = Valor(num=value)
    valor.save()
    return render(request, 'index.html')

def post(request):
    if request.method == 'POST':
        num = request.POST.get('num')

        valor = Valor(num=num)
        valor.save()
        return HttpResponse('FODA')