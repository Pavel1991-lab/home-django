# Generated by Django 4.2.4 on 2023-08-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_blog_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=150, verbose_name='slug'),
        ),
    ]
