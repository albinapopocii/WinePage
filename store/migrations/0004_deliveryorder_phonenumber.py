# Generated by Django 3.1.4 on 2020-12-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201206_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryorder',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
