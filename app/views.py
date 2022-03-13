from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import detail_form,user_form,singin_form
from .models import user_details
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
# Create your views here.
def singup(request):
    if request.method == 'POST':
        user = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_type = request.POST['User_Type']
        image = request.FILES['image']
        address = request.POST['address']
        us1 = User.objects.create_user(user, email, password1)
        us1.first_name=fname
        us1.last_name=lname
        us1.save()
        user = User.objects.get(username=user)
        us2 = user_details(user=user,User_Type=user_type, image=image, address=address)
        us2.save()
        return redirect('singin')
    return render(request,'singup.html',{'user_form':user_form,'detail_form':detail_form})

def singin(request):
    if request.method == "POST":
        username = request.POST['User_name']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            us = User.objects.get(username = request.user)
            us1 = user_details.objects.get(user= request.user)
            return render(request,'dash.html',{'user':us,'detail':us1})
        else:
            HttpResponseRedirect('/')
    else:
        fm = singin_form
        return render(request, 'singin.html',{'form':fm})