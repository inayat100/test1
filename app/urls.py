from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.singup,name='singup'),
    path('login/',views.singin,name='singin'),
]