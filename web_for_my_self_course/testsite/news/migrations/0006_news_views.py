# Generated by Django 3.2.2 on 2021-05-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]