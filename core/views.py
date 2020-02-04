from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse("<h1>Hello {}</h1>".format(nome))

def soma(request,a,b):
    soma = a + b
    return HttpResponse("O resultado da soma é: {}".format(soma))

def subtracao(request,a,b):
    subtracao = a - b
    return HttpResponse("O resultado da Subtração é: {}".format(subtracao))

def multiplicacao(request,a,b):
    multiplicacao = a * b
    return HttpResponse("O resultado da Multiplicação é: {}".format(multiplicacao))

def divisao(request,a,b):
    divisao = a / b
    return HttpResponse("O resultado da Divisão é: {}".format(divisao))
