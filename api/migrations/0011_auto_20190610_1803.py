# Generated by Django 2.2.2 on 2019-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190610_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingmessage',
            name='status',
            field=models.CharField(default='Not Responded', max_length=40),
        ),
    ]