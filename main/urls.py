from django.urls import path 
from main.views import index,yd
urlpatterns = [
    path("",index,name="index"),

]