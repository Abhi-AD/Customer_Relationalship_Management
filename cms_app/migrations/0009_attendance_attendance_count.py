# Generated by Django 4.2.5 on 2023-12-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0008_plan_subscription_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance_count',
            field=models.IntegerField(default=0),
        ),
    ]