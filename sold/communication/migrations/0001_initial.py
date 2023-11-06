# Generated by Django 4.2.7 on 2023-11-06 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communications', to='item.item')),
                ('members', models.ManyToManyField(blank=True, related_name='communications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
            },
        ),
        migrations.CreateModel(
            name='CommunicationMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='communication.communication')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]