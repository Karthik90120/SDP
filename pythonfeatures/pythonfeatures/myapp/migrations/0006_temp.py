# Generated by Django 5.0 on 2024-04-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('hum', models.FloatField()),
            ],
            options={
                'db_table': 'Weather_Description',
            },
        ),
    ]
