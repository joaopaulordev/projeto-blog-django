from django.shortcuts import render
from .models import *

def index(request):
    funcionarios = Funcionario.objects.order_by('nome')

    context = {"funcionarios": funcionarios}
    return render(request, 'blog/index.html', context)
