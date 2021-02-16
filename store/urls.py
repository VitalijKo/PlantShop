from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
	path('', views.store, name = 'store'),
	path('products/', views.products, name = 'products'),
	path('price/', views.price, name = 'price'),
	path('contacts/', views.contacts, name = 'contacts'),
	path('services/', views.services, name = 'services'),
	path('gallery/', views.gallery, name = 'gallery'),
	path('<int:product_id>/', views.detail, name = 'detail'),
	path('s<int:sproduct_id>/', views.sdetail, name = 'sdetail'),
	path('<slug:url>/', views.product_category, name = 'product_category'),
	path('s/<slug:surl>/', views.sproduct_category, name = 'sproduct_category'),
]
