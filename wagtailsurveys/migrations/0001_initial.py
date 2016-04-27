# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_data', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='submit time')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'form submission',
            },
        ),
    ]
