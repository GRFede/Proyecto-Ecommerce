# Generated by Django 5.1.2 on 2024-11-04 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_delete_productos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personas',
            old_name='nacimiento',
            new_name='edad',
        ),
    ]