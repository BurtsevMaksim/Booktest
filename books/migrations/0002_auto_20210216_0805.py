# Generated by Django 3.1.6 on 2021-02-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='book',
            name='poster_image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]