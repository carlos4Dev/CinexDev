# Generated by Django 2.1.2 on 2021-01-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0005_auto_20201210_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='Imagen',
            field=models.URLField(default=0, help_text='De imdb mismo'),
        ),
    ]
