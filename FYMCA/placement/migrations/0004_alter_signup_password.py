# Generated by Django 3.2.9 on 2023-02-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0003_auto_20230207_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
