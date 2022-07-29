from django.shortcuts import render,get_object_or_404
from receitas.models import Receita
from django.contrib.auth.models import User
from django.db.models import Q




def busca(request):
    """ Cria a pagina com as receitas buscadas pelo usuario"""
    if 'filtro' in request.GET:
        if request.user.is_authenticated:
            id = request.user.id
            receitas = Receita.objects.filter(Q(publicada=True) | Q(pessoa=id)).filter(nome_receita__icontains=request.GET['filtro'])
            dados = {
                'receitas': receitas
            }
            return render(request, 'receitas/buscar.html', dados)
        else:
            receitas = Receita.objects.filter(publicada=True).order_by('-date_receita').filter(nome_receita__icontains=request.GET['filtro'])
            dados = {
                'receitas': receitas
            }
            return render(request, 'receitas/buscar.html', dados)

    else:
        return render(request, 'receitas/buscar.html')