# Generated by Django 4.2.2 on 2023-07-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_categoria_nombre_publicaciones_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='update',
            field=models.DateField(auto_now=True),
        ),
    ]
