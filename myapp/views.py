from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from decimal import Decimal
from .models import Expenditure, User  # Importing required models
from django.views.generic import ListView

# Basic Views
def home(request):
    return render(request, 'home.html')

def expenses(request):
    return render(request, 'expenses.html')

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from decimal import Decimal, InvalidOperation
from .models import Expenditure  # Ensure Expenditure model is imported

# Expenditure Views
def add_expenditure(request):
    """
    View for adding a new expenditure. Handles POST request for form submission and
    GET request to display the form.
    """
    if request.method == 'POST':
        # Capture the form data from the request
        category = request.POST.get('category')
        type_ = request.POST.get('type')
        date = request.POST.get('date')
        amount = request.POST.get('amount')

        try:
            # Convert amount to Decimal for accurate storage
            amount = Decimal(amount)
            
            # Create and save a new expenditure entry
            Expenditure.objects.create(
                category=category,
                type=type_,
                date=date,
                amount=amount
            )

            # Redirect to expenditure list after successful creation
            return redirect('expenditure-list')  # Ensure this URL name exists in your urls.py

        except (ValueError, InvalidOperation):
            # Render form with error if amount conversion fails
            return render(request, 'add-expenditure.html', {
                'error': 'Invalid amount entered. Please enter a valid number.',
                'category': category,
                'type': type_,
                'date': date,
                'amount': amount,  # Preserve the input values for user convenience
            })

    # Render the form for GET requests
    return render(request, 'add-expenditure.html')


def expenditure_list(request):
    """
    View to display a list of all expenditures.
    """
    expenditures = Expenditure.objects.all()
    return render(request, 'expenditure-list.html', {'expenditures': expenditures})


# User Views
def register(request):
    """
    View for registering a new user.
    """
    if request.method == 'POST':
        # Capture user details from form
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        password = (request.POST['password'])  # Encrypt the password before saving
        
        # Create and save new user instance
        User.objects.create(email=email, mobile=mobile, role=role, password=password)

        messages.success(request, 'User registered successfully!')
        return redirect('register')  # Redirect to a relevant page, such as login or home page

    return render(request, 'registration.html')


def user_list(request):
    """
    View to display a list of all users.
    """
    users = User.objects.all()  # Fetch all users
    return render(request, 'userslist.html', {'users': users})

from django.shortcuts import render, redirect
from .models import User  # Assuming you have a custom user model

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")  # Debugging output
        try:
            user = User.objects.get(email=email)
            print(f"User found: {user}")  # Debugging output
            print(user.password)
            if user.password == password:  # Direct comparison (not secure)
                # login(request, user)  # Log the user in
                print("Password matched")
                if(user.role=="Viewer"):
                    # return redirect('user-expenditure-list') 
                    expenditures = Expenditure.objects.all()
                    return render(request,'user/expenditure-list.html',{'role':user.role, 'expenditures': expenditures})
                else:
                    # return redirect('index') 
                    return render(request, 'index.html', {'role': user.role})
                    
            else:
                error = "Invalid email or password."
                print("Password mismatch")  # Debugging output
        except User.DoesNotExist:
            error = "Invalid email or password."
            print("User does not exist")  # Debugging output
        
        return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')





def user_expenditure_list(request):
    """
    View to display a list of all expenditures.
    """
    expenditures = Expenditure.objects.all()
    return render(request, 'user/expenditure-list.html', {'expenditures': expenditures})
