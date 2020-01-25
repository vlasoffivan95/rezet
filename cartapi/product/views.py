# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404, JsonResponse
from .models import *


# Create your views here.
def api_product(request, id):

	product = get_object_or_404(Product, pk=id)

	img = []
	for image in product.get_images():
		img.append(str(image.image))

	response = {
		'category': product.category.name,
		'brand': product.brand.name,
		'name': product.name,
		'price': int(product.price),
		'description': product.description,
		'images': img,
	}
	
	return JsonResponse(response, content_type="application/json; charset=utf-8")

def home(request):

	products = Product.objects.all()
	cart_count = 0

	if 'cart' in request.session:
		cart_count = request.session['cart']['allcount']

	return render(
		request, 
		'index.html', 
		{
			'products':products,
			'cart_count': cart_count,
		}
	)

