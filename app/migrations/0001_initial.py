# Generated by Django 5.1.2 on 2024-11-02 04:45

import app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hex_color', models.CharField(default='#2778a9', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tags', models.ManyToManyField(blank=True, null=True, to='app.tag')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('FAILED', 'Failed'), ('SKIPPED', 'Skipped')], max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('crontab', models.CharField(max_length=100, validators=[app.models.validate_crontab])),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task')),
            ],
        ),
    ]
