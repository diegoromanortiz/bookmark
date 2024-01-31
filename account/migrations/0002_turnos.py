# Generated by Django 4.2 on 2023-06-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('motivoConsulta', models.TextField(blank=True, max_length=80)),
                ('elijeTurno', models.DateTimeField(unique=True)),
            ],
        ),
    ]
