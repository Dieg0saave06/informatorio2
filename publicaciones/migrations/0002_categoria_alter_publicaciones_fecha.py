# Generated by Django 4.2.2 on 2023-07-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
