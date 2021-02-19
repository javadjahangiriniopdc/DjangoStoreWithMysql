# Generated by Django 3.1.6 on 2021-02-19 09:34

from django.db import migrations, models
import orderapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.FileField(upload_to='files/user_avatar', validators=[orderapp.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.FileField(upload_to='files/product_cover', validators=[orderapp.models.validate_file_extension]),
        ),
    ]