# Generated by Django 2.0.1 on 2018-04-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databse', '0005_auto_20180404_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quickDescript',
            field=models.TextField(default='desc', help_text='Enter a brief description of the product', max_length=200),
            preserve_default=False,
        ),
    ]
