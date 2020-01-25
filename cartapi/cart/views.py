from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404, JsonResponse
from .models import *
from product.models import *
from .forms import *

# Create your views here.
def add_to_cart(request):

	# del request.session['cart']

	product_id = request.GET.get('id', '')

	if 'cart' in request.session:
		if str(product_id) in request.session["cart"].keys():
			request.session["cart"][str(product_id)] += 1
		else:
			request.session['cart'][str(product_id)] = 1
		request.session['cart']['allcount'] = request.session['cart']['allcount'] + 1
		request.session.modified = True
	else:
		request.session['cart'] = {}
		request.session['cart'][str(product_id)] = 1
		request.session['cart']['allcount'] = 1
		request.session.modified = True

	return HttpResponse('ok')

def cart(request):

	cart_item = []
	allprice = 0
	if 'cart' in request.session:
		for i in request.session['cart']:
			if i != 'allcount':
				product = Product.objects.get(id=i)
				count = request.session['cart'][i]
				price = product.price * int(request.session['cart'][i])
				allprice += price
				cart_item.append({
					'product': product,
					'count': count,
					'price': price
				})

	return render(
		request,
		'cart.html',
		{
			'cart_item': cart_item,
			'allprice': allprice,
		}
	)


def edit_count_cart(request):

	id = request.GET.get('id', '')
	type = request.GET.get('type', '')

	if id and type and 'cart' in request.session:
		if type == 'minus':
			request.session['cart'][str(id)] -= 1
			request.session['cart']['allcount'] = request.session['cart']['allcount'] - 1
			request.session.modified = True
		else:
			request.session['cart'][str(id)] += 1
			request.session['cart']['allcount'] = request.session['cart']['allcount'] + 1
			request.session.modified = True

	return HttpResponse('ok')

def delete_cart(request):

	id = request.GET.get('id', '')
	if id and 'cart' in request.session:
		request.session['cart']['allcount'] = request.session['cart']['allcount'] - request.session['cart'][str(id)]
		del request.session['cart'][str(id)]
		request.session.modified = True

	return HttpResponse('ok')

def shipping(request):

	allprice = 0

	try:
		default_delivery = TypeDelivery.objects.filter(active_default=True)[0].id
	except:
		default_delivery = 1

	try:
		more_delivery = TypeDelivery.objects.filter(active_more=True)[0].id
	except:
		more_delivery = 1

	delivery = TypeDelivery.objects.all()

	if 'cart' in request.session:
		for i in request.session['cart']:
			if i != 'allcount':
				product = Product.objects.get(id=i)
				count = request.session['cart'][i]
				price = product.price * int(request.session['cart'][i])
				allprice += price

	if request.method == 'POST':
		form = OrderForm(request.user, request.POST)
		if form.is_valid():
			order = form.save()
			order.price = order.shipping_options.price + allprice
			order.price_shipping = order.shipping_options.price
			order.save()
			if 'cart' in request.session:
				for i in request.session['cart']:
					if i != 'allcount':
						product = Product.objects.get(id=i)
						order_product = OrderProduct(order=order, product=product, price=product.price, count=int(request.session['cart'][i]))
						order_product.save()
				del request.session['cart']
				request.session.modified = True

		return HttpResponsePermanentRedirect('/thanks/')

	form = OrderForm(request.user)

	return render(
		request, 
		'shipping.html', 
		{
			'form': form,
			'allprice': allprice,
			'default_delivery': default_delivery,
			'more_delivery': more_delivery,
			'delivery': delivery,
		}
	)


def thanks(request):

	return render(
		request,
		'thanks.html',
		{}
	)






