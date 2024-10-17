from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

def loginPage(request):
    if request.method == "GET":
        return render(request, 'frontend/loginPage.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('pagina')
        else:
            return render(request, 'frontend/loginPage.html', {'error': 'Credenciais inválidas'})

def cadastroPage(request):
    if request.method == "GET":
        return render(request, 'frontend/cadastroPage.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        error_messages = []

        # Os 2 if's vão verificar se o email e o nome já existe
        if User.objects.filter(email=email).exists():
            error_messages.append('Email já cadastrado.')

        #esse aki também
        if User.objects.filter(username=name).exists():
            error_messages.append('Nome de usuário já cadastrado.')

        # Se houver erro ele vai renderiza a pagina novamente
        if error_messages:
            return render(request, 'frontend/cadastroPage.html', {'error': ' '.join(error_messages)})
                        #O adm do site
                #Usuario: Admindeteste     senha: testeadm
                
                #É so colocar /admin depois da url
                
        
        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            return redirect('login')  
        except ValidationError as e:
            return render(request, 'frontend/cadastroPage.html', {'error': str(e)})
        except Exception as e:
            return render(request, 'frontend/cadastroPage.html', {'error': f'Erro ao cadastrar usuário: {str(e)}'})

@login_required
def pagina(request):
    return render(request, 'frontend/pagina.html')