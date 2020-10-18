# Generated by Django 2.0.4 on 2019-12-13 10:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_book_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='format',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='is_available',
            field=models.BooleanField(default=True, help_text='Is the books available to buy?'),
        ),
        migrations.AlterField(
            model_name='books',
            name='published_date',
            field=models.DateField(blank=True, help_text='Please enter the date in <b>YYYY-MM-DD</b> format.', null=True),
        ),
    ]