# Generated by Django 3.2.20 on 2023-07-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_monitors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computers',
            old_name='description',
            new_name='operating_system',
        ),
    ]
