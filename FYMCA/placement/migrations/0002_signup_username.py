# Generated by Django 3.2.9 on 2023-02-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='username',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
