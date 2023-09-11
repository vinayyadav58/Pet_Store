# from django.contrib import admin
# from .models import pet
# from django.utils.html import format_html
# from django.conf import settings

# class customadmin(admin.ModelAdmin):
#     list_display = ["name","breed","img_display"]
#     list_filter = ["gender"]

#     def img_display(self,obj):
#         return format_html('<img src = "{}" width = "90" height = "100"/>',obj.image.url)

# # Register your models here.
# admin.site.register(pet,customadmin)
# admin.site.site_header = "pets app admin panels"
# admin.site.site_title = "Welcome to pet_store"
# admin.site.index_title = "Pets app admin"

from django.contrib import admin
from .models import pet
from cart.models import cart
from orders.models import Orders,Payment,OrderPet
from django.utils.html import format_html
from django.conf import settings


class ordercustom(admin.ModelAdmin):
    list_display = ['user','status']

class paymentcustom(admin.ModelAdmin):
    list_display = ['payment_id','status']


class customadmin(admin.ModelAdmin):
    list_display = ['name','species','breed','img_display']
    list_filter = ['gender','age']
    search_fields = ['species']



    def img_display(self,obj):
        return format_html('<img src="{}" width="90" height="100"/>',obj.image.url)


# Register your models here.

admin.site.register(pet,customadmin)
admin.site.register(cart)
admin.site.register(OrderPet)
admin.site.register(Payment,paymentcustom)
admin.site.register(Orders,ordercustom)
admin.site.site_header = "pets app admin panel"

admin.site.site_title = "welcome to petstore"

admin.site.index_title = "pet app admin"