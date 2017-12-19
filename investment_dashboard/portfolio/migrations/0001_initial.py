# Generated by Django 2.0 on 2017-12-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('equityType', models.CharField(max_length=10)),
                ('equityName', models.CharField(max_length=30)),
                ('units', models.DecimalField(decimal_places=10, max_digits=20)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
    ]
