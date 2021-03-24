from datetime import datetime

import django
from django.contrib.auth.base_user import BaseUserManager
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
    avatar = models.FileField('عکس', upload_to='user_avatar', null=True, blank=True,
                              validators=[validate_file_extension])
    description = RichTextField('توضیحات')

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name


class Product(models.Model):
    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    title = models.CharField('عنوان', max_length=50, null=False, blank=False)
    cover = models.FileField(upload_to='product_cover', validators=[validate_file_extension],
                             verbose_name='کاور کالا', null=True, blank=True)
    price = models.IntegerField('قیمت', default=0)
    description = RichTextField('توضیحات')
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


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, sex, show_cell_phone, user_name, email, cell_phone, expired, is_admin,
                    password=None):
        """
            Creates and saves a User with the given email, phone and password.
        """
        if not user_name:
            raise ValueError('user must have username')
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            user_name=user_name,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
