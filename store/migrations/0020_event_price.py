# Generated by Django 3.1.4 on 2020-12-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20201210_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.FloatField(max_length=20, null=True),
        ),
    ]