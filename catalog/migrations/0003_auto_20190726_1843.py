# Generated by Django 2.2.3 on 2019-07-27 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190726_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]