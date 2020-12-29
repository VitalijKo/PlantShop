from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
	path('', views.store, name = 'store'),
	path('<int:product_id>/', views.detail, name = 'detail'),
	path('<slug:url>/', views.product_category, name = 'product_category'),
]
