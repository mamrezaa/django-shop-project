# Generated by Django 5.2.1 on 2025-06-30 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='visits',
            field=models.IntegerField(default=0, verbose_name='تعداد مشاهده'),
        ),
    ]
