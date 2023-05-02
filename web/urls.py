from django.urls import path,include
from . import views

urlpatterns = [
    path("rooms/<int:id>",views.index,name="rooms"),
    path("room_details/<int:id>",views.room_details,name="room"),
    path("booking",views.booking,name="booking"),
    path("",views.hotels,name="home"),
    path("res_hotels",views.res_hotels,name="res_hotels"),
    path("restaurant/<int:id>",views.restaurant,name="restaurant"),
    path("pool_hotels",views.pool_hotels,name="pool_hotels"),
    path("pools/<int:id>",views.pool,name="pools"),
    path("employees",views.employees,name="employees"),
    path("myrooms",views.myrooms,name="myrooms")

]
