# Generated by Django 2.0.1 on 2018-04-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databse', '0006_product_quickdescript'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='city', max_length=100),
            preserve_default=False,
        ),
    ]
