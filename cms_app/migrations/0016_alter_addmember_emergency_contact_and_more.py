# Generated by Django 4.2.5 on 2023-12-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0015_addmember_contact_addmember_emergency_contact2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmember',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='addmember',
            name='emergency_contact2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
