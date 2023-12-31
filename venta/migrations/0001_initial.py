# Generated by Django 4.2.7 on 2023-11-15 14:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('persona_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas_cliente', to='usuario.persona', verbose_name='Cliente')),
                ('persona_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas_vendedor', to='usuario.persona', verbose_name='Vendedor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_total', models.PositiveIntegerField(default=0, verbose_name='Cantidad Total')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Valor Total')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_venta_producto', to='productos.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_venta', to='venta.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name_plural': 'Detalles Venta',
            },
        ),
    ]
