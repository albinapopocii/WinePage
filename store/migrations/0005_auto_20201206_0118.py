# Generated by Django 3.1.4 on 2020-12-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_deliveryorder_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
