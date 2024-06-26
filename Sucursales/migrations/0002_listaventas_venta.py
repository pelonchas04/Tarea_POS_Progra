# Generated by Django 5.0.4 on 2024-05-05 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaVentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_venta', models.IntegerField()),
                ('id_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_venta', models.IntegerField()),
                ('id_sucursal', models.IntegerField()),
            ],
        ),
    ]
