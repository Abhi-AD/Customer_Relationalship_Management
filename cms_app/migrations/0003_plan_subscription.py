# Generated by Django 4.2.5 on 2023-12-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0002_displayprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('images', models.ImageField(upload_to='Price_subscription/%Y/%m/%d')),
            ],
        ),
    ]