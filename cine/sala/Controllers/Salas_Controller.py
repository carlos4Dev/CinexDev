from django.shortcuts import render, HttpResponse
from sala.Models.Salas_Models import Salas_Models
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Salas_Controller():
    def index(request):
        filtrar = None
        if request.method == "POST":
            filtrar = request.POST.get('filtrar')
        salas_list = Salas_Models.salas_list(filtrar)
        paginator = Paginator(salas_list, 4)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {'salas_list' : items}
        return render(request, 'views/salas/listado.html',context)

    def detalleSala(request,numero):
        objects = Salas_Models.getsala(numero)
        context = {'sala' : objects}
        return render(request, 'views/salas/detalleSala.html',context)

    def cartelera(request):
        filtrar = None
        if request.method == "POST":
            filtrar = request.POST.get('filtrar')
        peliculas_list = Salas_Models.peliculas_list(filtrar)
        # No tengo claro como declarar items, sin paginator
        paginator = Paginator(peliculas_list, 4)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {'peliculas_list' : items}
        return render(request, 'views/salas/cartelera.html',context)
   