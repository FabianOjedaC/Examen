# Generated by Django 2.1.3 on 2018-12-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=30)),
                ('direccionTienda', models.CharField(max_length=30)),
                ('ciudadTienda', models.CharField(max_length=30)),
                ('comunaTienda', models.CharField(max_length=30)),
                ('correoTienda', models.EmailField(max_length=254)),
            ],
        ),
    ]
