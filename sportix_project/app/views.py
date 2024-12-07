from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

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
    return render(req,'login.html')

def register(req):
    return render(req,'register.html')





# ----------------------------------admin---------------------------------------

def shop_home(req):
    return render(req,'admin/shop_home.html')