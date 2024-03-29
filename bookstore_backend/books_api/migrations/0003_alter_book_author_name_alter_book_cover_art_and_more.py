# Generated by Django 4.0.5 on 2022-06-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0002_book_author_name_book_cover_art_book_genre_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_art',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
