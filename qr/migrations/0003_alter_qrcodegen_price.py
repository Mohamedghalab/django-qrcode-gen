# Generated by Django 4.0.3 on 2022-03-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_alter_qrcodegen_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodegen',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
