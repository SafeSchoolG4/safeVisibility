# Generated by Django 2.1.3 on 2018-11-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visibility', '0003_auto_20160211_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='adresse_rue',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='adresse_ville',
            field=models.CharField(max_length=30),
        ),
    ]
