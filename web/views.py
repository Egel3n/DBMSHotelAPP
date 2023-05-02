from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from web.forms import SignupForm
from web.models import *
from django.contrib.auth.models import User
from .models import Guest,Room,BookingRelation
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request,id):
      rooms = Room.objects.filter(hotel = Hotel.objects.get(id=id)).filter(is_taken=False)
      if request.user.is_authenticated:
            guest = Guest.objects.get(user=request.user)
            return render(request,"index.html",{"rooms":rooms,"budget":guest.budget})
      else:
            guest = "Önce Giriş Yapmalısınız."
      
      return render(request,"index.html",{"rooms":rooms,"budget":"giriş yap önce"})

def room_details(request,id):
      room = Room.objects.get(id = id)
      if request.user.is_authenticated:
            guest = Guest.objects.get(user=request.user)
            return render(request,"room_details.html",{"room":room,"budget":guest.budget})   
      
      else:
            return render(request,"room_details.html",{"room":room,"budget":"giriş yap önce"})
      
@login_required(login_url="login")
def booking(request):
      if request.user.is_authenticated:
            checkin = request.POST["checkin"]
            checkout = request.POST["checkout"]
            checkin = datetime.strptime(checkin,'%Y-%m-%d')
            checkout = datetime.strptime(checkout,'%Y-%m-%d')
            dayss = checkout - checkin
            dayss = int(dayss.days)
            roomId = request.POST["roomId"]
            guest = Guest.objects.get(user_id = request.user.id)
            room = Room.objects.get(id=roomId)
            if dayss < 0:
                  return render(request,"room_details.html",{"room":room,"error":"Tersten mi gidiyosun?"})
            if int(guest.budget) >= room.daily_price*dayss:
                  newBooking = BookingRelation.objects.create(guest=guest,room=room,checkinDate=checkin,checkOutDate=checkout)
                  newBooking.save()
                  room.is_taken = True
                  guest.budget -= room.daily_price*dayss
                  room.save()
                  guest.save()

                  return render(request,"success.html")
            else:
                  return render(request,"room_details.html",{"room":room,"error":f"Bakiye Yetersiz toplam:{room.daily_price*dayss}TL."})
      else:
            return redirect("login")


def hotels(request):
      content = {"hotels":Hotel.objects.all(),"btn_message":"Odaları Gör","goto":"rooms"}
      return render(request,"hotels.html",content)

def res_hotels(request):
      content = {"hotels":Hotel.objects.all(),"btn_message":"Restoranları Gör","goto":"restaurant"}
      return render(request,"rest_hotel.html",content)

def restaurant(request,id):
      restaurants = Restaurant.objects.filter(hotel = Hotel.objects.get(id=id))
      content= {"restaurants":restaurants,"hotel":Hotel.objects.get(id=id)}
      return render(request,"restaurants.html",content)

def pool_hotels(request):
      content={"hotels":Hotel.objects.all(),"btn_message":"Havuzları Gör","goto":"pools"}
      return render(request,"pool_hotels.html",content)

def pool(request,id):
      pools = Pool.objects.filter(hotel=Hotel.objects.get(id=id))
      content ={"pools":pools,"hotel":Hotel.objects.get(id=id)}
      return render(request,"pools.html",content)

def employees(request):
      employees = Employee.objects.all()
      data = {"employees":employees,"pools":PoolEmployeeRelation.objects.all(),"restaurants":RestaurantEmployeeRelation.objects.all()}
      return render(request,"employees.html",data)


def myrooms(request):
      if not request.user.is_authenticated:
            return redirect("login")
      else:
            bookings = BookingRelation.objects.filter(guest__user = request.user)
            return render(request,"myrooms.html",{"bookings":bookings})