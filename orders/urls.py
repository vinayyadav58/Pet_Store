from django.urls import path
from . import views 
app_name = "orders"
urlpatterns = [
    path("billing",views.place_order,name="place_order"),
    path('payment/',views.payments,name='payments')

]

