# Generated by Django 3.0 on 2019-12-26 13:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('findr', '0011_auto_20191226_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60, verbose_name='username')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='phone_number')),
                ('is_admin', models.BooleanField(default=False, max_length=6, verbose_name='staff_status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findr.User'),
        ),
    ]