# Generated by Django 2.1.3 on 2018-12-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_producto_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ImagenProducto',
            field=models.ImageField(upload_to='static/media/'),
        ),
    ]
