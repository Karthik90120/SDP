# Generated by Django 5.0 on 2024-04-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_temp1'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('hum', models.FloatField()),
                ('place', models.CharField()),
            ],
            options={
                'db_table': 'Weather',
            },
        ),
    ]
