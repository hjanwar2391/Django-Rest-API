# Generated by Django 4.2.3 on 2023-11-14 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_rename_published_date_bookmodel_first_pub_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookModel',
            new_name='BookStoreModel',
        ),
    ]
