from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')  
    return render (request, 'accounts/login.html')

def register(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already exista!')
                    return redirect ('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login( request,user)
                    messages.success(request, "You are now logged in!")
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, "you are registered successfully.")
                    return redirect ('login')
            
        else:
            messages.error(request, "Password is not match")
            return redirect ('register')
    else:
        return render (request, 'accounts/register.html')

def dashboard(request):
    if request.user.is_authenticated:
        
        user_inquary = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
        data ={
            'inquiries' : user_inquary, 
        }
        return render (request, 'accounts/dashboard.html', data)
    else:
         redirect('login')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out')
        return redirect ('home')
    return redirect('home')
