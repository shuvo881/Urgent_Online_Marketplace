# Generated by Django 4.2.5 on 2023-09-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='item_images/'),
        ),
    ]
