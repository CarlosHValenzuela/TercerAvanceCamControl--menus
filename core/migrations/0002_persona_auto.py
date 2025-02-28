# Generated by Django 5.1.1 on 2024-10-15 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('R', 'Residente'), ('V', 'Visita')], default='R', max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id_auto', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=100)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.persona')),
            ],
        ),
    ]
