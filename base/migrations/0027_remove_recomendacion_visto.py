# Generated by Django 4.1.7 on 2023-04-19 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_recomendacion_visto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recomendacion',
            name='visto',
        ),
    ]
