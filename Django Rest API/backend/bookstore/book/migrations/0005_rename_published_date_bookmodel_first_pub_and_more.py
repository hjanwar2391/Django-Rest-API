# Generated by Django 4.2.3 on 2023-11-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_rename_last_pub_bookmodel_last_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='published_date',
            new_name='first_pub',
        ),
        migrations.RenameField(
            model_name='bookmodel',
            old_name='last_updated',
            new_name='last_pub',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='title',
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='book_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='category',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Sci-Fi', 'Sci-Fi'), ('Humor', 'Humor'), ('Horror', 'Horror')], max_length=30),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]