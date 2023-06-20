from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.index, name='us'),
    path('create' ,views.create ,name ='create'),
    path('<str:pk>' , views.go, name='go'), 
]
