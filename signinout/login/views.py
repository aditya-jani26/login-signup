from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import HttpResponse
#----------------------------------------------------------------
# Create your views here. I will write all funtion here for each url
def home(request):
    return render(request,'home.html')
#----------------------------------------------------------------
#If the user comes back...
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if user.objects.filter(email=email,password=password).exists():
            request.session['email_id'] = email
            return redirect('database')
        elif user.objects.filter(email=email).exists():
            return HttpResponse("password not found")
        elif user.objects.filter(password=password).exists():
            return HttpResponse("email not found")
        else:
            return HttpResponse("You Identifcation is not there please to go Registration")
        
    return render(request,'login.html')
#----------------------------------------------------------------
#Here new user is registered
def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = user(name=name,email=email,password=password)
        new_user.save()
        return redirect("login")
    return render(request,'registration.html')
#----------------------------------------------------------------
#This is used to call all data which is in database
def database(request):
    if 'email_id' in request.session.keys():
        emp = Employees.objects.all()
        print ("emp", emp)
        detail = {
            'emp':emp,
        }
        return render(request,'database.html',detail)
    else:
        return redirect('login')
#----------------------------------------------------------------
#This is used to add "new" Employees to database

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        addEmp = Employees(name=name, email=email, address=address, phone=phone)
        addEmp.save()
        return redirect('database')

    return render(request,'database.html')
#----------------------------------------------------------------

#This function is responsible for changes to be made in old database

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        updateemp = Employees(id=id, name=name, email=email, address=address, phone=phone)  
        updateemp.save()  
        return redirect('database')    

    return render(request,'database.html')

#----------------------------------------------------------------
#This is used for "deleteing" data from the database

def delete(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()

    detail = {
        'emp':emp
    }
    return redirect('database') 
#----------------------------------------------------------------
# This is used to remove cookies from the session so that after logout data is safe

def logout(request):
    del request.session['email_id']
    return redirect('login')