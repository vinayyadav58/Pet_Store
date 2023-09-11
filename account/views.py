from django.shortcuts import render,redirect
from .forms import registrationForm
from django.contrib import messages
from petsapp.views import pets_list
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy


# Create your views here.

def register(request):
    if request.method == 'GET':
         form = registrationForm()
         return render(request,'base/register.html',{'form_data':form})

    if request.method == 'POST':
         form = registrationForm(request.POST)
         if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request," Account created succesfully for user" ,user_name)
            return redirect('pets_list')

         else:
            messages.error(request,"OOPS some issue in your form")
            return render(request,'base/register.html',{'form_data':form})
        
    return render(request,'base/register.html',{'form_data':form})


class myloginview(LoginView):
    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully ")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request," invalid details ")
        return super().form_invalid(form)
    
class mylogout(LogoutView):
    def get_next_page(self):
        messages.success(self.request,"logged out successfully ")
        return reverse_lazy('home')
