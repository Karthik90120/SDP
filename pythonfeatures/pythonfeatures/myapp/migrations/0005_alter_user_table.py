# Generated by Django 5.0 on 2024-04-26 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]