# Generated by Django 3.1 on 2020-08-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20200824_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='joy_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
