# Generated by Django 5.1.3 on 2024-12-06 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_games'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]