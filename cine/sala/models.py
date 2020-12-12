from django.db import models

# Create your models here.
class Peliculas(models.Model):
    PeliculaId = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    Anio = models.IntegerField(default=0, verbose_name="Año")
    Pais = models.CharField(max_length=50)
    Duracion = models.IntegerField(default=0)
    Sipnosis = models.TextField()

    class Meta:
        verbose_name_plural = "Peliculas"

    def __str__(self):
        return self.Titulo

class ProgramacionSala(models.Model):
    SalaId = models.AutoField(primary_key=True)
    Numero = models.IntegerField(default=0, verbose_name="Sala")
    Capacidad = models.IntegerField(default=0)
    PeliculaId = models.ForeignKey(Peliculas, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Pelicula")
    Horario = models.DateTimeField(blank=True, null=True)
    Disponible = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Programación Sala"
        verbose_name_plural = "Programación Salas"

    def __str__(self):
        return str(self.Numero)