# Generated by Django 2.2.5 on 2020-03-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200317_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=30),
        ),
    ]
