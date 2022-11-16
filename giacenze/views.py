from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pc, Telefono
from .forms import FormGiacenzaPC, FormGiacenzaTelefono, Periferiche
# Create your views here.


def giacenze(request):
    """ view per vedere le giacenze in magazzino"""
    computers = Pc.objects.all()
    telefonini = Telefono.objects.all()

    context = {
        'computers': computers,
        'telefonini': telefonini,        
    }
    return render(request, 'giacenze/giacenze.html', context)


def aggiungipc_in_giacenza(request):
    """ 
    view per renderizzare form di aggiunta pc  
    se il form è valido le informazioni vengono salvate
    altrimenti è da ricompilare
    """
    prodotto = "PC"
    if request.method == "POST":
        # Creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormGiacenzaPC(request.POST)        
        if form.is_valid():
            pc = form.save()
            pc.save()
            avviso = f"Il {form.cleaned_data['modello']} è stato aggiunto"
        else:
            avviso = "non è possibile aggiungere il PC"
            return redirect('aggiungi_pc') 
    else:
        form = FormGiacenzaPC()
    context = {
        'form':form,
        'prodotto':prodotto
        }
    return render(request, 'giacenze/aggiungiprodotto.html', context)


def aggiungitelefono_in_giacenza(request):
    """ 
    view per renderizzare form di aggiunta telefono  
    se il form è valido le informazioni vengono salvate
    altrimenti è da ricompilare
    """
    prodotto = "TELEFONO"
    if request.method == "POST":
        form = FormGiacenzaTelefono(request.POST)        
        if form.is_valid():            
            avviso = f"Il {form.cleaned_data['modello']} è stato aggiunto"            
        else:
            avviso = f"non è possibile aggiungere il {prodotto}"
    else:
        form = FormGiacenzaTelefono()
    context = {
        'form':form,
        'prodotto':prodotto
        }
    return render(request, 'giacenze/aggiungiprodotto.html', context)


def modifica_periferiche(request):
    """
    view per renderizzare form 
    """
    prodotto = "PERIFERICHE"
    if request.method == "POST":
        form = Periferiche(request.POST)        
    else:
        form = Periferiche()
    context = {
        'form':form,
        'prodotto':prodotto
        }
    return render(request, 'giacenze/aggiungiperiferiche.html', context)



    