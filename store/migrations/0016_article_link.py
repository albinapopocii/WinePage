# Generated by Django 3.1.4 on 2020-12-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_article_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
