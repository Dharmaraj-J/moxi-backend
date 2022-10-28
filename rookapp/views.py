from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here



def homepage(request):
    return render(request,'homepage.html')




def spage(request):
     if request.method=='POST':
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            


            

            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('spage')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'userneme alraedy existes')
                return redirect('spage')
            else:        
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/')
        
     else:
        return render(request,'spage.html')        
