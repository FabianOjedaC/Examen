# Generated by Django 2.1.3 on 2018-12-10 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181210_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='empleado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='empleado', to='blog.Empleado'),
            preserve_default=False,
        ),
    ]
