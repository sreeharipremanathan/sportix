from django.urls import path
from . import views
urlpatterns=[
    path('',views.s_login),
    path('registeration',views.register),
    path('shop',views.shop_home)

]