from django.db import models
from ..models import Peliculas,ProgramacionSala

class Salas_Models():
    def salas_list(filtrar):
        if filtrar == None:
            salas = ProgramacionSala.objects.order_by('Numero','Horario')
        else:
            salas = ProgramacionSala.objects.filter(Nombre__contains=filtrar)
        return salas

    def getsala(numero):
        sala = ProgramacionSala.objects.get(SalaId=numero)
        return sala
    
    def peliculas_list(filtrar):
        if filtrar == None:
            peliculas = Peliculas.objects.order_by('Titulo')
        else:
            peliculas = Peliculas.objects.filter(Nombre__contains=filtrar)
        return peliculas