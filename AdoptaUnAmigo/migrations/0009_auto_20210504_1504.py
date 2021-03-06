# Generated by Django 3.1.7 on 2021-05-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptaUnAmigo', '0008_moreinfousers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfousers',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moreinfousers',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='moreinfousers',
            name='ciudad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='moreinfousers',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='media/Sin-foto-de-perfil-en-Facebook.jpg', null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
