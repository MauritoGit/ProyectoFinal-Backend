# Generated by Django 4.1.7 on 2023-04-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_pelicula_director_pelicula_nacionalidad_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='image',
            field=models.ImageField(default=0, upload_to='files/movies'),
            preserve_default=False,
        ),
    ]