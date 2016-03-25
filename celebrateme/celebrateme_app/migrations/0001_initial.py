# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 21:10
from __future__ import unicode_literals

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
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=600)),
                ('survived_by', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('url_slug', models.SlugField(max_length=100)),
                ('dob', models.DateField()),
                ('dod', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=250)),
                ('source', models.ImageField(upload_to='deceased_pics')),
                ('deceased_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrateme_app.Deceased')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400)),
                ('author', models.CharField(max_length=200)),
                ('deceased_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrateme_app.Deceased')),
            ],
        ),
        migrations.AddField(
            model_name='biography',
            name='deceased_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrateme_app.Deceased'),
        ),
    ]
