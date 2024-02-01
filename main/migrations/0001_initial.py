# Generated by Django 5.0.1 on 2024-01-30 17:54

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('publish_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='Изображение поста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['created_date'],
            },
        ),
    ]
