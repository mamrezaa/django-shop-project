# Generated by Django 5.2.1 on 2025-06-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='about',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='درباره ما'),
        ),
    ]
