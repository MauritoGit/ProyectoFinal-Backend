# Generated by Django 4.1.7 on 2023-03-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pelicula_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(choices=[('Accion', 'Accion'), ('Terror', 'Terror'), ('Drama', 'Drama'), ('Documental', 'Documental'), ('Comedia', 'Comedia'), ('Romantica', 'Romantica')], max_length=10),
        ),
    ]