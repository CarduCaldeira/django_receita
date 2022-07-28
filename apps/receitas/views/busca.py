from django.shortcuts import render
from receitas.models import Receita

def busca(request):
    """ Cria a pagina com as receitas buscadas pelo usuario"""
    if 'filtro' in request.GET:
        receitas = Receita.objects.filter(publicada=True).order_by('-date_receita').filter(nome_receita__icontains=request.GET['filtro'])
        dados = {
            'receitas': receitas
        }
        return render(request, 'receitas/buscar.html', dados)
    else:
        return render(request, 'receitas/buscar.html')