# Generated by Django 2.0.3 on 2018-04-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_auto_20180416_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
