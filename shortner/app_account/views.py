from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
# Create your views here.
def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        rememberme=request.POST.get("rememberme")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"username not found")
            return redirect("signin")
            
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            if rememberme:
                request.session.set_expiry(120000)
            else:
                request.session.set_expiry(0)
            next=request.POST.get("next",'')
            return redirect('home')
        else:
            messages.error(request,"paassword doesnt match")
            return redirect('signin')    
    next=request.GET.get('next',"")
    return render(request,'signin.html')

def register(request):
     if request.method == "POST":
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"user name already exist try with other username")
                return redirect("register")
        
            if User.objects.filter(email=email).exists():
                messages.error(request," email already exist try with other email address")
                return redirect("register")
            try:
                validate_password(password1)
                User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,username=username)
                messages.success(request,"account created succesfully")
                return redirect("signin")
            except ValidationError as e:
                for i in e.messages:
                    messages.error(request,i)
                return redirect("register")
            
        else:
            messages.error(request,"password and conform password doesnt match!")
            return redirect('register')

     return render(request,'register.html')

def signout(request):
    logout(request)
    return redirect('signin')