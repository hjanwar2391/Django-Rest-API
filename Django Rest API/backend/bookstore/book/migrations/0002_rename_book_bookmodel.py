# Generated by Django 4.2.3 on 2023-11-14 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='BookModel',
        ),
    ]
