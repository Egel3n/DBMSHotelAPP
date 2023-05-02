from django.contrib import admin
from web.models import *

# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    pass

class GuestAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class RoomGuestRelAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass
class RestaurantAdmin(admin.ModelAdmin):
    pass
class PoolAdmin(admin.ModelAdmin):
    pass
class EmployeeRestaurantAdmin(admin.ModelAdmin):
    pass
class EmployeePoolAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Guest,HotelAdmin)
admin.site.register(Room,HotelAdmin)
admin.site.register(BookingRelation,RoomGuestRelAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Pool,PoolAdmin)
admin.site.register(RestaurantEmployeeRelation,EmployeeRestaurantAdmin)
admin.site.register(PoolEmployeeRelation,EmployeePoolAdmin)


