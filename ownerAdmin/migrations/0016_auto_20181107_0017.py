# Generated by Django 2.1.3 on 2018-11-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerAdmin', '0015_auto_20181107_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=models.ImageField(blank=True, default='roomImages/room3.jpg', null=True, upload_to='roomImages'),
        ),
    ]
