from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from web.models import Guest
from django.contrib import messages


# Create your views here.

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.SUCCESS,"Başarıyla Giriş Yapıldı")
            
            return redirect("home")
        else:
            return render(request,'account/login',{'error':'yanlis bir seyler var.'})
        


    return render(request,"account/login.html")


def register_request(request):
    if request.method == "POST":
        fname = request.POST["firstName"]
        lname = request.POST["lastName"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        mail = request.POST["mail"]
        budget =   int(request.POST["budget"])

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{'error':"Username Already In Use"})
            else:
                if User.objects.filter(email=mail).exists():
                    return render(request,"account/register.html",{'error':"Mail Already In Use"})
                else:
                    user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=mail,password=password)
                    user.save()
                    guest = Guest.objects.create(user=user,budget=budget)
                    guest.save()
                    redirect("home")
        else:
            return render(request,"account/register.html",{'error':"Passwords Not Matched"})


    return render(request,"account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")