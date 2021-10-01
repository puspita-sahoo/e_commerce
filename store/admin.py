from django.contrib import admin
from .models import Product, Address, Cartitem


admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Cartitem)
