from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article.html')

def categorie(request):
    return render(request, 'categorie.html')

def vente(request):
    return render(request, 'vente.html')

def stock(request):
    return render(request, 'stock.html')