# Generated by Django 3.0 on 2019-12-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20191216_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='joy_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
