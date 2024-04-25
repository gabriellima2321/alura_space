from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from apps.galeria.models import Fotografia 
from apps.galeria.forms import FotografiaForms
from django.contrib.auth.models import User
from django.contrib import auth,messages

def index(request):
    if request.user.is_authenticated:
        fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
        return render(request, 'galeria/index.html', {"cards": fotografias})
    else:
        return redirect('login')


def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Nova fotografia cadastrada!')
            return redirect('home')

    return render(request, 'galeria/nova_imagem.html', {'form':form})


def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request,'Informações editadas com sucesso!')
            return redirect('home')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Foto eliminada com sucesso!!')
    return redirect('home')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})