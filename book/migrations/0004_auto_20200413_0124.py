# Generated by Django 3.0.5 on 2020-04-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_comment_mark_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='', max_length=255),
        ),
    ]
