# Generated by Django 3.1 on 2020-12-09 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peliculas',
            options={'verbose_name_plural': 'Peliculas'},
        ),
        migrations.AlterModelOptions(
            name='programacionsala',
            options={'verbose_name': 'Programación Sala', 'verbose_name_plural': 'Programación Salas'},
        ),
        migrations.AddField(
            model_name='programacionsala',
            name='Horario',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='Anio',
            field=models.IntegerField(default=0, verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='programacionsala',
            name='Numero',
            field=models.IntegerField(default=0, verbose_name='Sala'),
        ),
        migrations.AlterField(
            model_name='programacionsala',
            name='PeliculaId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sala.peliculas', verbose_name='Pelicula'),
        ),
    ]
