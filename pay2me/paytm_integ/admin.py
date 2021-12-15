from django.contrib import admin
from .models import *


# Register your models here.


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'ammount', 'payment_status')


admin.site.register(OrderDetails, OrderDetailsAdmin)
