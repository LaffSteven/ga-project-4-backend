# Generated by Django 4.0.5 on 2022-06-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0020_alter_book_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
