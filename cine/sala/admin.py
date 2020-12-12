from django.contrib import admin
from .models import Peliculas, ProgramacionSala

# Register your models here.
admin.site.register(Peliculas)

class SalasAdmin(admin.ModelAdmin):
    list_display = ("Numero","PeliculaId","Capacidad","Horario","Disponible")
    search_fields =("Numero",)
    list_filter = ("Numero","PeliculaId","Horario")
    #date_hierarchy = ()

admin.site.register(ProgramacionSala,SalasAdmin)
