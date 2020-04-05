from django.contrib import admin
from .models import Inventory, Customer, Item, Orders, Payment, UserProfile

# Register your models here.

admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Orders)
admin.site.register(Payment)
admin.site.register(UserProfile)
