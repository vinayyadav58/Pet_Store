from django.urls import path
from  .import views

urlpatterns =[
    path('pets_list/',views.pets_list,name="pets_list"),
    path('pets_details/<int:pk>' ,views.pets_details,name="pet_detail"),
    path('dog-list/',views.dog_list,name="dog-list"),
    path('cat-list/',views.cat_list,name="cat-list"),
    path('search/',views.search_list,name="search-list"),


]