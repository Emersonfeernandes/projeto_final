# Generated by Django 3.2.9 on 2021-11-28 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211128_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url_scraper',
            old_name='URL',
            new_name='URL_save',
        ),
    ]
