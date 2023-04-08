from django.shortcuts import render,HttpResponse,redirect
from vaccine.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    #return HttpResponse("this is home page")
    return render(request,'index.html')

    
def service(request):
    #return HttpResponse("this is service page")
    return render(request,'service.html')
def contact(request):
   # return HttpResponse("this is contact page")  
   return render(request,'contact.html')
def register (request):
   # return HttpResponse("this is contact page")  
   return render(request,'register.html')
    
def slotbooking(request):  
   return render(request,'slotbooking.html') 
def slotcheck(request):  
   return render(request,'slotcheck.html')    
   
   

