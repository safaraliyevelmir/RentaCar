# Generated by Django 3.2.6 on 2021-08-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_condtion_req_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformationPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
    ]