# Generated by Django 4.1 on 2022-09-05 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'historial',
                'verbose_name_plural': 'historiales',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cedula', models.IntegerField(verbose_name='Documento de Identidad')),
                ('telefono', models.CharField(max_length=70, verbose_name='Telefono')),
                ('email', models.CharField(max_length=250, verbose_name='Correo Electronico')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('Rolid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.rol')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cedula', models.IntegerField(verbose_name='Documento de Identidad')),
                ('telefono', models.CharField(max_length=70, verbose_name='Telefono')),
                ('fechaNac', models.DateTimeField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('historialid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.historial')),
            ],
        ),
    ]