# Generated by Django 5.0.3 on 2024-03-13 01:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='hello@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='joining',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
