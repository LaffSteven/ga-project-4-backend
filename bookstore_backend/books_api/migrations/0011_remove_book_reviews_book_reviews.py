# Generated by Django 4.0.5 on 2022-06-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0010_remove_book_reviews_book_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reviews',
        ),
        migrations.AddField(
            model_name='book',
            name='reviews',
            field=models.ManyToManyField(to='books_api.review'),
        ),
    ]
