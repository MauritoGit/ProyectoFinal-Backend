# Generated by Django 4.1.7 on 2023-04-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_recomendacion_visto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacion',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
