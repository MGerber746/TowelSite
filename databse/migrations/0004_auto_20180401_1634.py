# Generated by Django 2.0.1 on 2018-04-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databse', '0003_auto_20180401_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='templates/products/%Y/%m/%d'),
        ),
    ]
