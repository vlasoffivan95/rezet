from django.db import models
from product.models import Product

# Create your models here.

class TypeDelivery(models.Model):

	name = models.CharField(max_length=250, verbose_name="Название", default='', blank=True)
	price = models.DecimalField(verbose_name="Цена", default=0, blank=True, null=True, max_digits=12, decimal_places=2)
	active_more = models.BooleanField(default=False, blank=True, verbose_name="Активный если цена больше 300€")
	active_default = models.BooleanField(default=False, blank=True, verbose_name="Активный по умолчанию")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Типы доставки"

class Order(models.Model):

	name = models.CharField(max_length=250, verbose_name="Name", default='', blank=True)
	address = models.CharField(max_length=300, verbose_name="Adress", default='', blank=True)
	phone = models.CharField(max_length=300, verbose_name="Phone", default='', blank=True)
	email = models.CharField(max_length=300, verbose_name="E-mail", default='', blank=True)
	shipping_options = models.ForeignKey(TypeDelivery, related_name='order_delivery', verbose_name=u"доставка", on_delete=models.SET_NULL, null=True)
	price_shipping = models.DecimalField(verbose_name="Цена доставки", default=0, blank=True, null=True, max_digits=12, decimal_places=2)
	price = models.DecimalField(verbose_name="Цена", default=0, blank=True, null=True, max_digits=12, decimal_places=2)

	class Meta:
		verbose_name_plural = "Заказы"


class OrderProduct(models.Model):

	order = models.ForeignKey(Order, related_name='order_product_order', verbose_name=u"Заказ", on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, related_name='order_product_product', verbose_name=u"Продукт", on_delete=models.SET_NULL, null=True)
	price = models.DecimalField(verbose_name="Цена", default=0, blank=True, null=True, max_digits=12, decimal_places=2)
	count = models.IntegerField(verbose_name="Количество", default=0, blank=True)
	
	class Meta:
		verbose_name_plural = "Продукты заказов"
