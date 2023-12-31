# Generated by Django 4.2.7 on 2023-11-07 09:58

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=86, scale=1, size=[600, 600], upload_to='images', verbose_name='Картинка'),
        ),
    ]
