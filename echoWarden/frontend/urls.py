from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('cadastro/', views.cadastroPage, name='cadastro'),
    path('pagina/', views.pagina, name='pagina'),
]





#          AQUI É UM CODIGO DE CADASTRO PARA CASO A FUNÇÃO DO VIEWS.PY DE ALGUM PROBLEMA!!
"""
def cadastroPage(request):
    if request.method == "GET":
        return render(request, 'frontend/cadastroPage.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verifica se o email já está cadastrado
        #SE DER ERRO APAGA ESSES 2 IF'S DE VERIFICAÇÕES
        if User.objects.filter(email=email).exists():
            return render(request, 'frontend/cadastroPage.html', {'error': 'Email já cadastrado.'})

        # Verifica nome de usuário já cadastrado
        if User.objects.filter(username=name).exists():
            return render(request, 'frontend/cadastroPage.html', {'error': 'Nome de usuário já cadastrado.'})
                #ATÉ AKI
    
                #É
                        #O adm do site
                #Usuario: Admindeteste     senha: testeadm
        
        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            return redirect('loginPage')
        except ValidationError as e:
            return render(request, 'frontend/cadastroPage.html', {'error': str(e)})
        except Exception as e:
            return render(request, 'frontend/cadastroPage.html', {'error': f'Erro ao cadastrar usuário: {str(e)}'})
"""