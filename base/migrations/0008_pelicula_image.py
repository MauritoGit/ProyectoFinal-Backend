# Generated by Django 4.1.7 on 2023-04-01 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_pelicula_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='image',
            field=models.ImageField(default=0, upload_to='files/movies'),
            preserve_default=False,
        ),
    ]