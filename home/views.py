from django.shortcuts import render

# Create your views here.
def index(request):
    ''' funzione per renderizzare la homepage'''
    return render(request, "home/index.html")
