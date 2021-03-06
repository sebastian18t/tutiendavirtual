# Generated by Django 3.1 on 2020-08-08 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField(auto_now_add=True, verbose_name='Fecha compra')),
                ('estado', models.BooleanField(default=False, verbose_name='proceso Completado')),
                ('dirc', models.CharField(max_length=50, verbose_name='Direccion entrega')),
                ('cliente_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProd', models.CharField(max_length=80, verbose_name='Nombre producto')),
                ('precio', models.FloatField(verbose_name='Precio modena colombiana')),
                ('imagen', models.URLField(max_length=286, verbose_name='URL imagen')),
                ('disponible', models.BooleanField(default=True, verbose_name='Producto Activo/Inactivo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha registro')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ItemsCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad comprada')),
                ('fecha_compra', models.DateField(auto_now_add=True, verbose_name='Fecha compra producto')),
                ('compra_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.compra')),
                ('producto_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.producto')),
            ],
            options={
                'verbose_name': 'ItemCompra',
                'verbose_name_plural': 'Itemscompra',
            },
        ),
    ]
