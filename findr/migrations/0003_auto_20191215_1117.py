# Generated by Django 3.0 on 2019-12-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findr', '0002_auto_20191215_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]