# Generated by Django 4.1.7 on 2023-04-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_pelicula_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='image',
            field=models.ImageField(default='none', upload_to='base/seriesPIC'),
            preserve_default=False,
        ),
    ]