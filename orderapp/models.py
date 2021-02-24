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
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='کاربر')
    avatar = models.FileField('عکس', upload_to='user_avatar', null=False, blank=False,
                              validators=[validate_file_extension])
    description = models.CharField('توضیحات', max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name


class Product(models.Model):
    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    title = models.CharField('عنوان', max_length=50, null=False, blank=False)
    cover = models.FileField(default='temp.jpg', upload_to='product_cover', validators=[validate_file_extension],
                             verbose_name='کاور کالا')
    price = models.IntegerField('قیمت', default=0)
    description = models.CharField('توضیحات', max_length=50, null=False, blank=False)
    create_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    update_at = models.DateTimeField('تاریخ ویرایش', auto_now=True)
    # create_at = models.DateTimeField(default=timezone.now)
    # create_at = models.DateTimeField(default=datetime.now)
    promote = models.BooleanField('تبلیغات', default=False)

    def __str__(self):
        return self.title


class OrderApp(models.Model):
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    title = models.CharField('عنوان', max_length=50, null=False, blank=False)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, verbose_name='مشتری')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='کالا')
    price = models.IntegerField(default=0)
    tedad = models.IntegerField(default=0)
    price_all = models.BigIntegerField(default=0)
    create_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    update_at = models.DateTimeField('تاریخ ویرایش', auto_now=True)
    # create_at = models.DateTimeField(default=timezone.now)
    # create_at = models.DateTimeField(default=datetime.now)
    description = RichTextField('توضیحات')

    def __str__(self):
        return self.title
