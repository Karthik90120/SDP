# Generated by Django 5.0 on 2024-04-27 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_temp1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp1',
            name='hum',
            field=models.CharField(),
        ),
    ]
