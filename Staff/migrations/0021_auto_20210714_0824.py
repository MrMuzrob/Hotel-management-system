# Generated by Django 3.1.12 on 2021-07-14 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0020_auto_20210713_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 14, 8, 24, 3, 637790, tzinfo=utc)),
        ),
    ]
