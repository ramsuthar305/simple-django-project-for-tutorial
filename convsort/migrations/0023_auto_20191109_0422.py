# Generated by Django 2.2 on 2019-11-08 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0022_auto_20191109_0408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrations',
            old_name='phone',
            new_name='roll_no',
        ),
    ]