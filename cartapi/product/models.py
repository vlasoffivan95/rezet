from django.db import models
from .fields import *
import random
from django.conf import settings
from cartapi.settings import BASE_DIR

def make_upload_path(instance, filename, prefix = False):
    # Переопределение имени загружаемого файла.
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    n4 = random.randint(0, 10000)
    n5 = random.randint(0, 10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3)+"_"+str(n4)+"_"+str(n5) + '.jpg'
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)

# Create your models here.

class Brand(models.Model):

	name = models.CharField(max_length=250, verbose_name="Название")

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Бренд"

class Category(models.Model):

	name = models.CharField(max_length=250, verbose_name="Название")

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Категории"

class Product(models.Model):

	category = models.ForeignKey(Category, related_name='product_category', verbose_name=u"категория", on_delete=models.SET_NULL, null=True)
	brand = models.ForeignKey(Brand, related_name='product_brand', verbose_name=u"бренд", on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=250, verbose_name="Название")
	price = models.DecimalField(verbose_name="Цена", default=0, blank=True, null=True, max_digits=12, decimal_places=2)
	description = models.TextField(blank=True, verbose_name="Краткое описание")

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_images(self):
		return ProductImage.objects.filter(product=self)

	class Meta:
		verbose_name_plural = "Продукт"

class ProductImage(models.Model):

	product = models.ForeignKey(Product, related_name='image_product', verbose_name=u"Продукт", on_delete=models.SET_NULL, null=True)
	image = ThumbnailImageField(upload_to=make_upload_path, blank=True,  verbose_name="изображение")

	def __unicode__(self):
		return self.product.name + str(self.id)

	def __str__(self):
		return self.product.name + str(self.id)

	class Meta:
		verbose_name_plural = "Фото продуктов"
		


