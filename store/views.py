from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import Category, Product, Pricelist, Gallery, SCategory, SProduct
from django.http import Http404, HttpResponseRedirect

def store(request):

	menu = Category.objects.all()

	context = {'menu': menu}

	return render(request, 'store/store.html', context)

def product_category(request, url):

	menu = Category.objects.all()

	products_list = Product.objects.filter(category__url=url)

	try:
		category_name = products_list[0].category.name
	except:
		category_name = 'Добавьте товар'

	products_count = products_list.count()

	context = {'object_list': products_list, 'category': category_name, 'count': products_count, 'menu': menu}

	return render(request, 'store/product_category.html', context)

def detail(request, product_id):

	menu = Category.objects.all()

	try:
		product = Product.objects.get(id = product_id)
	except:
		raise Http404('Товар с указанным ID не найден.')

	context = {'product': product, 'menu': menu}
	return render(request, 'store/detail.html', context)

def products(request):

	menu = Category.objects.all()

	context = {'menu': menu}

	return render(request, 'store/products.html', context)

def price(request):

	price = Pricelist.objects.all()

	context = {'price': price}

	return render(request, 'store/price.html', context)

def contacts(request):
	return render(request, 'store/contacts.html')

def services(request):
	menu = SCategory.objects.all()

	context = {'menu': menu}

	return render(request, 'store/services.html', context)

def gallery(request):

	gallery = Gallery.objects.all()

	context = {'gallery': gallery}

	return render(request, 'store/gallery.html', context)

def sproduct_category(request, surl):

	menu = SCategory.objects.all()

	products_list = SProduct.objects.filter(category__url=surl)

	try:
		category_name = products_list[0].category.name
	except:
		category_name = 'Добавьте услугу'

	products_count = products_list.count()

	context = {'object_list': products_list, 'category': category_name, 'count': products_count, 'menu': menu}

	return render(request, 'store/sproduct_category.html', context)

def sdetail(request, sproduct_id):
	menu = SCategory.objects.all()

	try:
		product = SProduct.objects.get(id = sproduct_id)
	except:
		raise Http404('Услуга с указанным ID не найден.')

	context = {'product': product, 'menu': menu}
	return render(request, 'store/sdetail.html', context)
