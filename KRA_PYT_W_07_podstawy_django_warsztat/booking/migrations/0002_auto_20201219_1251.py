# Generated by Django 3.1.3 on 2020-12-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='projector',
            field=models.BooleanField(default=False),
        ),
    ]
