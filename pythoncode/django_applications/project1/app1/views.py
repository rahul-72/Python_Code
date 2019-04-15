from django.shortcuts import render
from django.http import HttpResponse
from . import forms 
from app1.models import User 
def index(request):
    e = "Please Sign In to Enjoy Our Services"
    return render(request,'app1/index.html',{'error':e,'title':'HOME'})


def data(request):
    return render(request,'app1/data.html',{'title':"data"})

def signup(request):
    return render(request,"app1/signup.html",{'title':'Signup'})

def login(request):
    if request.method == "POST" : 
        form = forms.Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try : 
                u1 = User.objects.get(email=email)
            except User.DoesNotExist as e : 
                return render(request,"app1/index.html",{'error':e,'title':'LOGIN'})
            else :
                if password == u1.password : 
                    data = { 
                        'First Name': u1.first_name,
                        'Last Name' : u1.last_name,
                        'Email' : u1.email,
                    }
                    
                    return render(request,'app1/profile.html',{'data':data,'title':'Profile'})
                else : 
                    e = "Invaid Password Try Again"
                    return render(request,'app1/index.html',{'error':e,'title':'HOME'})  

        else : 
            e = "Invalid Data Provided..Please Mind your Input"
            return render(request,'app1/index.html',{'error':e,'title':'HOME'})       
    else : 
        e = "Request Method Does Not Allowed"
        return render(request,'app1/index.html',{'error':e,'title':'HOME'})

def mksignup(request):
    if request.method == "POST" : 
        form  = forms.Signup(request.POST)
        if form.is_valid() : 
            email = form.cleaned_data['email']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            password  = form.cleaned_data['password']
            try : 
                u1 = User.objects.get(email=email)
            except User.DoesNotExist as e : 
                user = User(email=email,first_name=fname,last_name=lname,password=password)
                user.save()
                return render(request,"app1/index.html",{'error':"Account sucessfully created please login to use our services",'title':'HOME'})
            else : 
                error = "User Already Exists"
                return render(request,'app1/index.html',{'error':error,'title':"HOME"})
        else : 
            error = "Invalid Form DATA"
            return render(request,'app1/index.html',{'error':error,'title':"HOME"})
        

    else : 
        error = "Invalid Form Method, We only accept POST"
        return render(request,'app1/index.html',{'error':error,'title':"HOME"})
        