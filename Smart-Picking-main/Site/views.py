import logging
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.shortcuts import redirect

# Importa a classe HttpResponse que é usada para retornar respostas HTTP simples.
# Importa a função render que é usada para renderizar templates HTML e retornar uma resposta.
# Importa o modelo User que representa usuários no sistema, permitindo criar, atualizar, deletar e consultar usuários.
# Importa o módulo messages que é usado para enviar mensagens de erro, sucesso, etc., para as views.
# Importa a função authenticate que é usada para verificar as credenciais de um usuário.

# Esta função renderiza a página de login quando a URL correspondente é acessada.
def home(request):
    return render(request, "login.html")

# Função para processar a tela de cadastro de usuários.
def Cadastro(request):
    # Se o método de requisição for GET (normalmente usado para acessar a página), apenas renderiza a página de cadastro.
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        # Caso o método seja POST (normalmente usado para enviar dados de um formulário), executa o cadastro.
        
        # Obtém os dados do formulário de cadastro usando request.POST.get(). Cada campo do formulário é capturado aqui.
        username = request.POST.get('name')
        email = request.POST.get('email')
        matricula = request.POST.get('matricula')
        senha = request.POST.get('password')

        # Verifica se já existe um usuário com o mesmo nome de usuário no banco de dados.
        userName = User.objects.filter(username=username).exists()
        userEmail = User.objects.filter(email=email).exists()
        userMatricula = User.objects.filter(first_name=matricula).exists()
    


        # Se o nome de usuário já estiver cadastrado, envia uma mensagem de erro e renderiza novamente a página de cadastro.

        if userName:
            messages.error(request, "Este Usuário já está Cadastrado.")
            return render(request, "cadastro.html")
        
        elif userEmail:
            messages.error(request, "Este Email já está Cadastrado.")
            return render(request, "cadastro.html")
        
        elif userMatricula:
            messages.error(request, "Essa Matricula já está Cadastrada.")
            return render(request, "cadastro.html")
        
        # Caso o usuário não exista, cria um novo usuário com os dados fornecidos.
        # Note que a matrícula é salva no campo first_name.
        user = User.objects.create_user(username=username, email=email, first_name=matricula, password=senha)

        # Envia uma mensagem de sucesso informando que o usuário foi cadastrado com sucesso.
        messages.success(request, 'Usuário Cadastrado com Sucesso.')
        
        # Após o cadastro, redireciona o usuário para a página de login.
        return redirect("Login")

# Função para renderizar a página de visualização do estoque.
def VizEstoque(request):
    return render(request, "VisualizarEstoque.html")

# Função para processar o login dos usuários.
# Nota: esta função contém um erro que precisa ser corrigido.
def Login(request):
    # Se o método de requisição for GET, renderiza a página de login.
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # Agora usamos 'email' para capturar o dado do formulário
        email = request.POST.get('email')
        senha = request.POST.get('password')

        # Verifica se os dados estão preenchidos
        if not email or not senha:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'login.html')

        # Autentica o usuário com base no email e senha
        user = authenticate(request, username=email, password=senha)

        if user is not None:
            if user.is_active:
                login_django(request, user)
                logging.info(f"Usuário {email} autenticado com sucesso. Redirecionando para 'dados'.")
                return redirect('dados')
            else:
                messages.error(request, "Conta desativada.")
                return render(request, 'login.html')
        else:
            logging.warning(f"Tentativa de login falhou para o usuário: {email}")
            messages.error(request, "Email ou senha incorretos.")
            return render(request, 'login.html')
        
        # elif user:
        #     # login_django(request, user)
        #     # logging.info("Usuário autenticado com sucesso. Redirecionando para 'dados'.")
        #     return HttpResponse('Entrou.')

        #     # return redirect('dados')

        # else:
        #     messages.error(request, "Email ou senha incorretos.")
        #     return render(request, 'login.html')
            
            
# Função para renderizar a página com dados da empresa.
def dados_empresa(request):
    if request.user.is_authenticated:

        return render(request, 'dadosDaEmpresa.html')
    else:
        
        return redirect('Login')
    
def cadastrarItens(request):
    return render(request, 'cadastrarItens.html')

def retirarItens(request):
    return render(request, 'retirarItens.html')

# Função para renderizar a página "guiratao".
def GuiRatão(request):
    return render(request, 'guiratao.html')
