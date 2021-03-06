# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-18 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('subTitle', models.CharField(max_length=255, verbose_name='Sous-titre')),
                ('enabled', models.BooleanField(default=False, verbose_name='Activer')),
                ('dateEvent', models.DateField(verbose_name="Date de l'evenement")),
                ('time', models.TimeField(default='00:00:00', verbose_name='Heure')),
                ('description', models.TextField(verbose_name='Description du projet')),
                ('location', models.CharField(max_length=255, verbose_name='Lieu')),
                ('presenter_picture', models.ImageField(upload_to='avatars_events', verbose_name='Presenter picture')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('first_right_picture', models.ImageField(blank=True, upload_to='avatars_events', verbose_name='First right picture')),
                ('second_right_picture', models.ImageField(blank=True, upload_to='avatars_events', verbose_name='Second right picture')),
                ('thanking_text', models.TextField(verbose_name='Texte de remerciment des partenaires.')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
