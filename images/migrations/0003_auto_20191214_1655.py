# Generated by Django 3.0 on 2019-12-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20191214_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_name']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='new_image',
        ),
    ]