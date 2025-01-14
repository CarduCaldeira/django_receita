from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """ Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print("O campo nome não pode ficar em branco")
            return redirect('cadastro')
        if not email.strip():
            print("O campo email não pode ficar em branco")
            return redirect('cadastro')
        if not senha.strip():
            print("O campo senha não pode ficar em branco")
            return redirect('cadastro')

        if senha != senha2:
            print("As senhas não são iguais")
            messages.error(request,'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print("Usuario ja cadastrado")
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            print("Usuario ja cadastrado")
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print(nome,email,senha,senha2)
        messages.success(request,'Cadastro realizado com sucesso')
        print('Usuario criado com sucesso')

        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de uma pessoa no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if not email.strip():
            print("O campo nome não pode ficar em branco")
            return redirect('login')
        if not senha.strip():
            print("O campo email não pode ficar em branco")
            return redirect('login')

        if User.objects.filter(email=email).exists():

            nome =User.objects.filter(email=email).values_list('username',flat=True).get()
            user =auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request,user)
                print('Login realizado')
                return redirect('dashboard')

            print('Senha incorreta')
            messages.error(request,'Senha Incorreta')
            return redirect('login')

        messages.error(request,'Email inexistente')
        print('email inexistente')
        return redirect('login')
    else:
        return render(request,'usuarios/login.html' )

def dashboard(request):
    """ Pagina de receitas criadas por ele de cada usuario"""
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {'receitas':receitas}

        return render(request,'usuarios/dashboard.html',dados)
    else:
       return redirect('index')

def logout(request):
    """ realiza o logout do sistema"""
    auth.logout(request)
    return redirect('index')






