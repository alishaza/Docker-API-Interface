# Generated by Django 4.1.2 on 2022-10-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Container_Name', models.CharField(max_length=200)),
                ('App_Name', models.CharField(max_length=200)),
                ('Image_Name', models.CharField(max_length=200)),
            ],
        ),
    ]
