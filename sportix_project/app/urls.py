from django.urls import path
from . import views
urlpatterns=[
    path('',views.s_login),
    path('registeration',views.register),
    path('logout',views.s_logout),




    # ________admin______
    path('shop',views.shop_home),
    path('add_pro',views.add_product),
    path('edit_pro/<id>',views.edit_pro),
    path('delete_pro/<id>',views.delete_pro),
    path('bookings',views.bookings),



# ---------user-------------
    path('user_home',views.user_home),
    path('view_pro/<id>',views.view_pro),
    path('add_to_cart/<id>',views.add_to_cart),
    path('cart_display',views.cart_display),
    path('delete_cart/<id>',views.delete_cart),
    path('buy_pro/<id>',views.buy_pro),
    path('view_bookings',views.view_bookings),
    path('contact',views.contact)


]