# Generated by Django 4.2.5 on 2023-12-14 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0014_alter_attendance_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmember',
            name='contact',
            field=models.CharField(default=datetime.datetime(2023, 12, 14, 9, 19, 49, 675858, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addmember',
            name='emergency_contact2',
            field=models.CharField(default=datetime.datetime(2023, 12, 14, 9, 20, 3, 917004, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
    ]
