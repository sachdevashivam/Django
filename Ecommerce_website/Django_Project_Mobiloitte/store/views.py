from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models.product import Product
from .models.customer import Customer
import re


# Create your views here.

def index(request):
    prds = Product.get_all_products()

    return render(request, 'index.html', {'products' : prds})



def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html') 

    else:
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phone')
        password1 = postData.get('password1')
        password2 = postData.get('password2')


        # Validation

        value = {
            'name' : name,
            'email' : email,
            'phone' : phone,
        }

        error_message = None

        customer = Customer(name = name,    
                            email = email,
                            phone = phone,
                            password1 = password1,
                            password2 = password2)

        
        if (not name):
            error_message = "Name Required !!"

        elif (not email):
            error_message = "Email Required !!"    

        elif (not '@' in email):    
            error_message = 'Enter Valid Email !!'

        elif (not phone):
            error_message = 'Phone Number Required !!'

        elif (len(phone) < 10) or (len(phone) > 10):
            error_message = 'Enter valid Phone Number !!'

        elif (not password1):
            error_message = 'Password Required !!'

        elif len(password1) < 8:
            error_message = 'Password should be 8 characters or more !!'   

        elif re.search('[0-9]',password1) is None:
            error_message = "Password should have atleast one number !!"

        elif re.search('[A-Z]',password1) is None: 
            error_message = "Password should have atleast one uppercase !!"  

        elif (not password2):
            error_message = "Please confirm your password !!"

        elif password2 != password1:
            error_message = "Password Doesn't Match !!"        


        elif customer.isExist():
            error_message = 'Email address already registered !!'


        
        # Saving
        if not error_message:
            customer.password1 = make_password(customer.password1)
        
            customer.register() 
            return redirect('home')  

        else:  
            data = {
                'error' : error_message,
                'values' : value
            }                  

            return render(request, 'signup.html', data)



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')


    else:
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        customer = Customer.get_customer_by_email(email)

        error_message = None

        if customer:
            flag = check_password(password1, customer.password1)
            if flag:    
                return redirect('home')
            else:
                error_message = 'Email or Password Invalid !!'

        else:
            error_message = 'Email or Password Invalid !!'


        return render(request, 'login.html', {'error' : error_message})



# def googlemap(request):
#     mapbox_access_token = 'pk.my_mapbox_access_token'
#     return render(request, 'googlemap.html', {'mapbox_access_token' : mapbox_access_token})





def nearest_restaurants(request):
    return render(request, 'nearest_restaurants.html')    