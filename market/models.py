from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import ForeignKey


class ProductCategory(models.Model):
   '''Категории Продукта'''

   name = models.CharField(max_length=180)

   class Meta:
      verbose_name_plural = 'Категории товаров'
      verbose_name = 'Категория товара'



class Product(models.Model):
   '''Модель Товара'''

   object = None
   category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='продукты')
   name = models.CharField(max_length=100)

   price = models.PositiveIntegerField(help_text='в сомах')
   sales_percent = models.PositiveSmallIntegerField(
      verbose_name='скидки',
      null=True,
      validators=[MaxValueValidator(100)]
   )

   description = models.TextField()
   preview_image = models.ImageField()

   new_expiry_date = models.DateField()

   def __str__(self):
      return self.name


   def get_price_with_sales(self):
      '''Возвращает цену с учётом скидки'''

      if self.price is None or self.sales_percent is None:
         return self.price

      if self.sales_percent == 0:
         return self.price

   class Meta:
      verbose_name_plural = 'Товары'
      verbose_name = 'Товар'



class ProductGallery(models.Model):
   gallery = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
   image = models.ImageField()

   class Meta:
      verbose_name_plural = 'Галерея товаров'
      verbose_name = 'Галерея товара'



