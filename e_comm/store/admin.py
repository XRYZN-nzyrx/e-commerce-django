from django.contrib import admin
from store.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartProduct)

