from datetime import datetime

import django
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

from django.utils import timezone


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.FileField(upload_to='files/user_avatar', null=False, blank=False,
                              validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    cover = models.FileField(upload_to='files/product_cover', null=False, blank=False,
                             validators=[validate_file_extension])
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=50, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # create_at = models.DateTimeField(default=timezone.now)
    # create_at = models.DateTimeField(default=datetime.now)
    promote = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OrderApp(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # create_at = models.DateTimeField(default=timezone.now)
    # create_at = models.DateTimeField(default=datetime.now)
    description = RichTextField()

    def __str__(self):
        return self.title
