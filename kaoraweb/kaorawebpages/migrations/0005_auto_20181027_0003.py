# Generated by Django 2.1.2 on 2018-10-27 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaorawebpages', '0004_auto_20181026_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
