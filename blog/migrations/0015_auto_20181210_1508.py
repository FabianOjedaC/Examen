# Generated by Django 2.1.3 on 2018-12-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181210_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='empleado',
            field=models.CharField(max_length=30),
        ),
    ]
