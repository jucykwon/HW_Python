# Generated by Django 4.1.7 on 2023-02-14 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='f.name', max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(db_column='l.name', max_length=50, verbose_name='Last name')),
                ('birthday', models.DateField(default=datetime.date(2023, 2, 14))),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group_description', models.TextField()),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
