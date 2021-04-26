from django.contrib import admin


from .models import merchants, Order

admin.site.register(merchants)
admin.site.register(Order)
