# Generated by Django 2.2.2 on 2019-11-08 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0018_auto_20191108_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 8, 17, 57, 31, 703962)),
        ),
    ]
