from django.urls import path
from . import views
urlpatterns=[
    path('',views.s_login),
    path('registeration',views.register),
    path('shop',views.shop_home),
    path('logout',views.s_logout),
    path('add_pro',views.add_product)

]