# Generated by Django 3.2.6 on 2021-08-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionForCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='catagory',
            name='img',
            field=models.ImageField(upload_to='cars/'),
        ),
    ]
