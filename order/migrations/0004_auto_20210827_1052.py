# Generated by Django 3.2.6 on 2021-08-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_child_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
