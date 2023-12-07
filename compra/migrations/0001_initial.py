# Generated by Django 4.2.7 on 2023-11-15 14:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Compra')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('precio_unidad', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Precio Unitario')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Valor Total')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('cantidad', models.PositiveIntegerField(default=0, help_text='La cantidad tiene que ser menor a 100', validators=[django.core.validators.MaxValueValidator(100)])),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.compra', verbose_name='Compra')),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.materia_prima', verbose_name='Materia Prima')),
            ],
            options={
                'verbose_name_plural': 'Detalle Compra',
            },
        ),
    ]
