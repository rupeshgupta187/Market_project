# Generated by Django 3.2.4 on 2023-09-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_product_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincategory',
            name='Mpic',
            field=models.ImageField(default='', upload_to='static/mcategory/'),
        ),
    ]
