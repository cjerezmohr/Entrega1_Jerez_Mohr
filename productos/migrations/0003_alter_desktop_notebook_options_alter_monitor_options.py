# Generated by Django 4.0.4 on 2022-06-07 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_monitor_periferico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='desktop_notebook',
            options={'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterModelOptions(
            name='monitor',
            options={'verbose_name': 'Monitor', 'verbose_name_plural': 'Monitores'},
        ),
    ]
