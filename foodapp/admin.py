from django.contrib import admin

# Register your models here.
from .models import Customer, Menu, Order

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Order)
