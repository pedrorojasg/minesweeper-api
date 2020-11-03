# Generated by Django 3.1.3 on 2020-11-03 00:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='field',
        ),
        migrations.AddField(
            model_name='game',
            name='field_board',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('', ''), ('m', 'm')], max_length=1), size=100), default=[], size=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_board',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('', ''), ('?', '?'), ('f', 'f'), ('x', 'x')], max_length=1), size=100), size=100),
        ),
    ]