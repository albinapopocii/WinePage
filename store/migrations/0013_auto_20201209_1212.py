# Generated by Django 3.1.4 on 2020-12-09 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_desscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desscription',
            new_name='description',
        ),
    ]