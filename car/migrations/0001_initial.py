# Generated by Django 3.2.6 on 2021-08-26 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='car/')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('fuel', models.CharField(choices=[('benzin', 'benzin'), ('dizel', 'dizel'), ('elektrik', 'elektrik')], max_length=255)),
                ('type_of_transmissions', models.CharField(choices=[('auto', 'auto'), ('mexanika', 'mexanika')], max_length=255)),
                ('engine', models.FloatField()),
                ('year', models.IntegerField(default=2000)),
                ('luggage', models.IntegerField()),
                ('seat_count', models.IntegerField()),
                ('door', models.IntegerField()),
                ('star_count', models.IntegerField()),
                ('price_2_3', models.CharField(max_length=255, verbose_name='Price for 2-3 Day')),
                ('price_4_7', models.CharField(max_length=255, verbose_name='Price for 4-7 Day')),
                ('price_7_15', models.CharField(max_length=255, verbose_name='Price for 7-15 Day')),
                ('price_16_30', models.CharField(max_length=255, verbose_name='Price 1for 6-30 Day')),
                ('price_30', models.CharField(max_length=255, verbose_name='Price for more 30 Day')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.catagory')),
            ],
        ),
    ]
