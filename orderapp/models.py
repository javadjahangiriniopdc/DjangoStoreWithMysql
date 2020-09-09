from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null=False, blank=False)
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    cover = models.FileField(upload_to='files/product_cover', null=False, blank=False)

    def __str__(self):
        return self.title


class OrderApp(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=datetime.now)
    description = RichTextField()

    def __str__(self):
        return self.title
