# Generated by Django 3.1.7 on 2021-04-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptaUnAmigo', '0005_anuncios_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncios_fav',
            name='anuncio',
            field=models.ManyToManyField(to='AdoptaUnAmigo.Anuncio'),
        ),
    ]
