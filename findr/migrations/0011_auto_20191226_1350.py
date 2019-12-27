# Generated by Django 3.0 on 2019-12-26 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('findr', '0010_auto_20191226_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='isNegotiable',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='bargained'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
