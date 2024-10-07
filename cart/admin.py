from django.contrib import admin

# Register your models here.
from .models import Product, CartItem,Category,Order

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Order)



