# Generated by Django 3.1 on 2020-08-09 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200809_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]