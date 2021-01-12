from django.contrib import admin
from .models import Category, Product, Pricelist, Gallery

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Pricelist)
admin.site.register(Gallery)
