# Generated by Django 3.1.4 on 2020-12-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_article_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
