# Generated by Django 5.1.1 on 2024-09-04 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'Галерея товара', 'verbose_name_plural': 'Галерея товаров'},
        ),
    ]