from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q

def store(request):

	menu = Category.objects.all()

	search_query = request.GET.get('search', '')
	if search_query:
		products_list = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
	else:
		products_list = Product.objects.all().order_by('id')

	paginator = Paginator(products_list, 18)
	page = request.GET.get('page')

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	is_paginated = products.has_other_pages()

	if products.has_previous():
		prev_url = '?page={}'.format(products.previous_page_number())
	else:
		prev_url = ''

	if products.has_next():
		next_url = '?page={}'.format(products.next_page_number())
	else:
		next_url = ''

	context = {'object_list': products, 'is_paginated': is_paginated, 'next_url': next_url, 'prev_url': prev_url, 'menu': menu}

	return render(request, 'store/store.html', context)

def product_category(request, url):

	menu = Category.objects.all()

	search_query = request.GET.get('search', '')
	if search_query:
		products_list = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
	else:
		products_list = Product.objects.filter(category__url=url)

	paginator = Paginator(products_list, 18)
	page = request.GET.get('page')

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	is_paginated = products.has_other_pages()

	if products.has_previous():
		prev_url = '?page={}'.format(products.previous_page_number())
	else:
		prev_url = ''

	if products.has_next():
		next_url = '?page={}'.format(products.next_page_number())
	else:
		next_url = ''

	context = {'object_list': products, 'is_paginated': is_paginated, 'next_url': next_url, 'prev_url': prev_url, 'menu': menu}

	return render(request, 'store/store.html', context)

def detail(request, product_id):

	menu = Category.objects.all()

	try:
		product = Product.objects.get(id = product_id)
	except:
		raise Http404('Товар с указанным ID не найден.')
		
	context = {'product': product, 'menu': menu}
	return render(request, 'store/detail.html', context)
