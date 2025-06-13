from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .models import Profile
def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        role = request.POST.get('role')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user_data_has_error = False
        
        # make sure email and username are not being used
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exists')

            # make aure password is at least 5 characters long
        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, 'Password must be at least 5 characters')

        if not user_data_has_error:
            new_user = User.objects.create_user(
                first_name = firstname,
                last_name = lastname,
                email = email,
                username = username,
                password = password
        )
            # Create Profile with phone and role
            Profile.objects.create(user=new_user, phone_num=phone, role=role)

            messages.success(request, 'Account created. Login now')
            return redirect('login')
        else:
            return render(request, 'signup.html')

    return render(request, 'signup.html')
        
def landing_page(request):
    return render(request,"landingpage.html")

def login_view(request):
    if request.method == 'POST':
     # getting user inputs from frontend
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
    # authenticate credentials
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                # login user if login credentials are correct
                login(request, user)
                # ewdirect to home page
                return redirect('home')
            else:
                # redirect back to the login page if credentials are wrong
                messages.error(request, 'Invalid email or password')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
        return redirect('login')
    return render(request, 'login.html')
@login_required # restrict page to authenticated users
def Home(request):
    return render(request, 'login.html')
# where authenticated user gets redirected to when they try to access a login required view
LOGIN_URL = 'login'

def LogoutView(request):

    logout(request)

    # redirect to login page after logout
    return redirect('login')
@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def settings_view(request):
    return render(request, 'settings.html')



@login_required
def my_listings_view(request):
    return render(request, 'my_listings.html')

@login_required
def rental_requests_view(request):
    return render(request, 'rental_requests.html')

@login_required
def search_properties_view(request):
    return render(request, 'search_properties.html')

@login_required
def favorites_view(request):
    return render(request, 'favorites.html')

@login_required
def my_rentals_view(request):
    return render(request, 'my_rentals.html')

def aboutus(request):
    return render(request,'aboutus.html')
def services(request):
    return render(request,'service.html')