# Generated by Django 3.0 on 2019-12-16 17:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('findr', '0003_auto_20191215_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('house_name', models.CharField(max_length=60, verbose_name='house_name')),
                ('house_pic', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=60, verbose_name='price')),
                ('isFurnished', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, verbose_name='furnished')),
                ('isParkingSpace', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, verbose_name='parkingspace')),
                ('isAvailable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='available')),
                ('isFenced', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='fenced')),
                ('isHaveWater', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='water')),
                ('isNewHouse', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='new')),
                ('isNegotiable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='new')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_type', models.CharField(max_length=60, verbose_name='')),
            ],
        ),
        migrations.DeleteModel(
            name='House',
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment_categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findr.ApartmentCategory'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findr.User'),
        ),
    ]
