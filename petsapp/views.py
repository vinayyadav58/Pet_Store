from django.shortcuts import render,HttpResponse
from .models import pet
from django.http import Http404
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def pets_list(request):
    pets_data = pet.objects.all()
    data = {'pets_d' : pets_data}
    return render(request,'petsapp/list.html',data)

def pets_details(request,pk):
    query = pet.objects.get(id=pk)
    # if query.exists() and query.count() == 1:
    #     instance = query.first()
    # else:
    #     return Http404("pet data does not exists")
    context = {
        "data":query
    }
    
    return render(request,"petsapp/details.html",context)

def dog_list(request):
    dog_data = pet.objects.filter(animal_type="d")
    all_dog_data = {
        "objectdog" : dog_data
    }

    return render(request,"petsapp/dog-list.html",all_dog_data)

def cat_list(request):
    cat_data = pet.objects.filter(animal_type="c")
    all_cat_data = {
        "objectcat" : cat_data
    }

    return render(request,"petsapp/cat-list.html",all_cat_data)



def search_list(request):
   search_query = request.GET.get('search')
   if len(search_query)>78:
       all_search = [ ]
   else :
    name_search = pet.objects.filter(name__icontains = search_query)
    breed_search = pet.objects.filter(breed__icontains = search_query)
    gender_search = pet.objects.filter(gender__icontains = search_query)
    price_search = pet.objects.filter(price__icontains = search_query)
    all_search = name_search.union(breed_search,gender_search,price_search)
    context = {
           "search" : all_search
           }
    return render(request,"petsapp/search_list.html",context)
   
#    if all_search.count() == 0:
#        messages.error(request,"No search result found ")

