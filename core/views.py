from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tecnologia(request):
    return render(request, 'tecnologia.html')

def perguntas(request):
    return render(request, 'perguntas.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def vantagens(request):
    return render(request, 'vantagens.html')

def ailson_team(request):
    return render(request, 'ailson_team.html')

def adjailson_team(request):
    return render(request, 'adjailson_team.html')

def daniel_team(request):
    return render(request, 'daniel_team.html')

def vanthuir_team(request):
    return render(request, 'vanthuir_team.html')

def sobre(request):
    return render(request, 'sobre.html')

def solucoes(request):
    return render(request, 'solucoes.html')

def suporte(request):
    return render(request, 'suporte.html')

def localizacao(request):
    return render(request, 'localizacao.html')

def contato(request):
    return render(request, 'contato.html')

# def login(request):
#     return render(request, 'login.html')

def login_view(request):
    return render(request, 'login.html')

