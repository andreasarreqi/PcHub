# Generated by Django 3.2.20 on 2023-07-27 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_delete_reviews'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Monitors',
        ),
    ]