# Generated by Django 4.2.7 on 2023-11-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=64, null=True, verbose_name='Slug'),
        ),
    ]
