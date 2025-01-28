from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def s_login(req):
    if 'shop' in req.session:
        # req.session.flush()
        return redirect(shop_home)
    else:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname     #create
                    return redirect(shop_home)
                else:
                    req.session['user']=uname
                    return redirect(user_home)
            else:
                messages.warning(req,'invalid username or password')
                return redirect(s_login)
    return render(req,'login.html')

def s_logout(req):
    logout(req)
    req.session.flush()
    return redirect(s_login)

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        send_mail('Accout Registration', 'Your Sportix account registration is successfull', settings.EMAIL_HOST_USER, [email])
        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
        except:
            messages.warning(req,'user details already exists')
            return redirect(register)
        return redirect(s_login)
    else:
        return render(req,'register.html')
    # return render(req,'register.html')





# ----------------------------------admin---------------------------------------

def shop_home(req):
    if 'shop' in req.session:
        product=Product.objects.all()
        # print(product)
        return render(req,'admin/shop_home.html',{'product':product})
    else:
        return render(s_login)
    

def add_product(req):
    if req.method=='POST':
        # id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST=['offer_price']
        file=req.FILES['img']
        data=Product.objects.create(pro_name=name,image=file,price=price,offer_price=offer_price)
        data.save()
        print(data)
    return render(req,'admin/add_product.html')


def edit_pro(req,id):
    print(id)
    pro=Product.objects.get(pk=id)
    if req.method=='POST':
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST['offer_price']
        file=req.FILES.get('img')
        print(file)
        if file:
            Product.objects.filter(pk=id).update(pro_name=name,price=price,offer_price=offer_price,image=file)
        else:
            Product.objects.filter(pk=id).update(pro_name=name,price=price,offer_price=offer_price)
        return redirect(shop_home)
    return render(req,'admin/edit_pro.html',{'data':pro})


def delete_pro(req,id):
    data=Product.objects.get(pk=id)
    url=data.image.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(shop_home)

def bookings(req):
    bookings=buy.objects.all()[::-1][:3]
    print(bookings)
    return render(req,'admin/bookings.html',{'data':bookings})

def admin_cancel_order(req,id):
    data =buy.objects.get(pk=id)
    data.delete()
    return redirect(bookings)





# ---------------user-----------------

def user_home(req):
    product=Product.objects.all()
    return render(req,'user/user_home.html',{'product':product})

def view_pro(req,id):
    product=Product.objects.get(pk=id)
    return render(req,'user/view_pro.html',{'product':product})

def add_to_cart(req,id):
    product=Product.objects.get(pk=id)
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.create(user=user,Product=product)
    data.save()
    return redirect(cart_display)

def cart_display(req):
    log_user=User.objects.get(username=req.session.get('user'))
    data=Cart.objects.filter(user=log_user)
    print(data)
    return render(req,'user/cart_display.html',{"data":data})

# def qty_in(req,cid):
#     data=Cart.objects.get(pk=cid)
#     data.qty+=1
#     data.price= data.qty*data.product.offer_price
#     data.save()
#     return redirect(cart_display)

def delete_cart(req,id):
    data=Cart.objects.get(pk=id)
    data.delete()
    return redirect(cart_display)

def buy_pro(req,id):
    product=Product.objects.get(pk=id)
    user=User.objects.get(username=req.session['user'])
    price=product.offer_price
    data=buy.objects.create(user=user,product=product,price=price)
    data.save()
    return redirect(user_home)


def view_bookings(req):
    user=User.objects.get(username=req.session['user'])
    data=buy.objects.filter(user=user)[::-1]
    return render(req,'user/view_bookings.html',{'data':data})

def cancel_order(req,id):
    data = buy.objects.get(pk=id)
    data.delete()
    return redirect(view_bookings)

def contact(req):
    return render(req,'user/contact.html')