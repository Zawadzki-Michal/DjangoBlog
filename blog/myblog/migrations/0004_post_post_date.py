# Generated by Django 5.0.2 on 2024-02-13 13:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Published'),
            preserve_default=False,
        ),
    ]
