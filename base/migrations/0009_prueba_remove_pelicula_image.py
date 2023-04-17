# Generated by Django 4.1.7 on 2023-04-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_pelicula_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='files/movies')),
            ],
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='image',
        ),
    ]