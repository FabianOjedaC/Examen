# Generated by Django 2.1.3 on 2018-12-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181210_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precioProducto',
            field=models.CharField(max_length=30),
        ),
    ]