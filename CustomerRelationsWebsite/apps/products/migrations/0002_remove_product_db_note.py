# Generated by Django 4.0.10 on 2023-12-11 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='db_note',
        ),
    ]