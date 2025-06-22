from django.shortcuts import render, redirect
from .models import Post,Autor,Categoria
from .forms import AutorForm,CategoriaForm,PostForm,BusquedaForm

def inicio(request):
    return render(request,'blog/inicio.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})
    
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def buscar_post(request):
    posts = []
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            if titulo:
                posts = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar.html', {'form': form, 'posts': posts})
