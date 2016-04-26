# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(max_length=140)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseType'),
        ),
    ]