# Generated by Django 4.2.7 on 2023-11-07 09:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=86, scale=1, size=[1200, 1200], upload_to='images', verbose_name='Картинка'),
        ),
    ]