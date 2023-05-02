from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=40)
    stars = models.IntegerField()
    img = models.ImageField(null=True,upload_to="uploads")

    def __str__(self) -> str:
        return self.name
    

class Room(models.Model):
    type = models.CharField(max_length=40,default="normal suit")
    number_of_beds = models.IntegerField()
    is_taken = models.BooleanField(default=False)
    daily_price = models.IntegerField()
    img = models.ImageField(null=True,upload_to="uploads")
    hotel = models.ForeignKey(Hotel,on_delete= models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.type
    
class Employee(models.Model):
    name = models.CharField(max_length=30,null=True)
    job = models.CharField(max_length=20,null= True)
    img = models.ImageField(null=True,upload_to="uploads")

    def __str__(self) -> str:
        return self.name

class Guest(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    budget = models.IntegerField(null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.user.first_name


class BookingRelation(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    checkinDate = models.CharField(max_length=20)
    checkOutDate = models.CharField(max_length=20)

    def __str__(self) -> str:
        return "guestName: "+self.guest.user.first_name +"  ||  "+" roomId: " +f'{self.room.id}'
    

class Restaurant(models.Model):
    hotel = models.ForeignKey(Hotel ,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    img = models.ImageField(null = True,upload_to="uploads")

    def __str__(self) ->str:
        return self.hotel.name+" "+self.name
    

class Pool(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    img = models.ImageField(null=True,upload_to="uploads")

    def __str__(self):
        return self.hotel.name + " " + self.type

class PoolEmployeeRelation(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    pool = models.ForeignKey(Pool,on_delete=models.CASCADE)
    hourly_wage = models.IntegerField(null=True)
    start_Date = models.DateField(null=True)

    def __str__(self)->str:
        return f"Employee: {self.employee.name} Pool: {self.pool.type}"

class RestaurantEmployeeRelation(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    hourly_wage = models.IntegerField(null=True)
    start_Date = models.DateField(null=True)

    def __str__(self)->str:
        return f"Employee: {self.employee.name} Restaurant: {self.restaurant.name}"
    

    



