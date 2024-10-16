from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
      # return HttpResponse("this is home page")
      return render(request,'index.html')

def about(request):
      # return HttpResponse("this is about page")
      return render(request,'about.html')

def services(request):
      # return HttpResponse("this is service page")
      return render(request,'services.html')

def contact(request):
      # return HttpResponse("this is contact page")
      if request.method=="POST":
            name=request.POST.get('name')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            desc=request.POST.get('desc')
            contact=Contact(name=name,phone=phone,email=email,desc=desc)
            contact.save()
            messages.success(request,'your message has been sent')
      return render(request,'contact.html')