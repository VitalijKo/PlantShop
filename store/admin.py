from django.contrib import admin
from .models import Category, Product, Pricelist, Gallery, SCategory, SProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SCategory)
admin.site.register(SProduct)
admin.site.register(Pricelist)
admin.site.register(Gallery)
