# Generated by Django 4.1.7 on 2023-04-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_comentario_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='puntaje',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]