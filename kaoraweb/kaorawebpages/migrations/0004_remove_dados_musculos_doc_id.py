# Generated by Django 2.1.2 on 2018-11-26 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kaorawebpages', '0003_auto_20181126_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados_musculos',
            name='doc_id',
        ),
    ]