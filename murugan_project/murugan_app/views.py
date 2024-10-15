from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import signin, ecom_model,Cart# Assuming these models exist
import random
import smtplib
from django.contrib import messages
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

def generate_otp(length=6):
    digits = "0123456789"
    OTP = "".join(random.choices(digits, k=length))
    return OTP

def product_page(request):
    # Ensure the user is logged in before accessing the product page
    if request.session.get('is_authenticated', False):
        products = ecom_model.objects.all()
        user_name = request.session.get('name', 'Guest')  # Fetch user name from session or use 'Guest'
        return render(request, "product.html", {"product": products, "user_name": user_name})
    else:
        return redirect('login')  # Redirect to login page if not authenticated

def send_otp_email(receiver_email, otp):
    sender_email = "classyshoppz@gmail.com"
    email_password = "zsju igvo mlnv icit"  # Use an app-specific password for security

    subject = f'Your OTP is {otp}'
    body = f'This is your OTP for Classy. The OTP is valid for 5 minutes. Your OTP is {otp}.'

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, email_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def sign_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Check if the email already exists in the database
        if signin.objects.filter(email=email).exists():
            return render(request, 'sigin_in.html', {'email_exists': True})

        # If email is unique, proceed with the sign-up process
        otp = generate_otp()
        request.session['name'] = name
        request.session['email'] = email
        request.session['phone_number'] = phone_number
        request.session['password'] = password
        request.session['otp'] = otp

        send_otp_email(email, otp)
        return render(request, 'verification.html', {'email': email})

    return render(request, 'sigin_in.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if otp == session_otp:
            name = request.session.get('name')
            email = request.session.get('email')
            phone_number = request.session.get('phone_number')
            password = request.session.get('password')
            
            # Store user details in the database after OTP verification
            signin.objects.create(name=name, email=email, phone_number=phone_number, password=password)
            
            # Clear session after storing the user details
            del request.session['name']
            del request.session['email']
            del request.session['phone_number']
            del request.session['password']
            del request.session['otp']

            # Redirect user to the login page after signup and OTP verification
            return redirect('login')
        else:
            return HttpResponse("Invalid OTP! Please check the valid OTP.")
    
    return render(request, 'verification.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if user exists and the credentials are correct
#         user = signin.objects.filter(email=email, password=password).first()
#         if user:
#             # Set user as authenticated and store the name in session
#             request.session['is_authenticated'] = True
#             request.session['name'] = user.name  # Save the user's name in the session
#             request.session['user_id'] = user.id
#             return redirect('product_page')
#         else:
#             return HttpResponse("Invalid login credentials")
    
#     return render(request, 'login.html') old login 
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = signin.objects.filter(email=email, password=password).first()
        if user:
            # Store the user's ID in session after successful login
            request.session['is_authenticated'] = True
            request.session['name'] = user.name
            request.session['user_id'] = user.id
            return redirect('product_page')  # Redirect to the products page
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    
    return render(request, 'login.html')


# def login(request):
#     if request.method == 'POST':
#         # Your custom login logic
#         username = request.POST['username']
#         password = request.POST['password']
        
#         try:
#             user = sign_in.objects.get(username=username, password=password)
#             request.session['user_id'] = user.id  # Store user ID in session
#             return redirect('products')  # Redirect after successful login
#         except sign_in.DoesNotExist:
#             # Handle login failure
#             return render(request, 'login.html', {'error': 'Invalid login'})
    
#     return render(request, 'login.html')


def some_view(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Render the template and the logged-in user's information will be available in the template automatically
        return render(request, 'product.html')
    else:
        # Redirect to login page if not authenticated
        return redirect('login')

def logout(request):
    # Log the user out by clearing the session
    request.session.flush()
    return redirect('index')
def index(request):
    return render(request,'index.html')

def resend_otp(request):
    email = request.session.get('email')
    if email:
        otp = generate_otp()
        request.session['otp'] = otp
        send_otp_email(email, otp)
        return render(request, 'verification.html', {'email': email})
    return HttpResponse("Error in resending OTP. Please try again.")

def add_to_cart(request, product_id):
    # Check if the user is logged in by checking the session
    if 'user_id' not in request.session:
        return redirect('login')  # Redirect to login page if not logged in

    # Get the user ID from the session
    user_id = request.session['user_id']
    
    # Fetch the user from your custom sign_in model
    user = get_object_or_404(signin, id=user_id)
    
    # Fetch the product
    product = get_object_or_404(ecom_model, id=product_id)
    
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    
    if created:
        # Set quantity to 1 if the item was newly created
        cart_item.quantity = 1
    else:
        # Only increment the quantity if the item already exists in the cart
        cart_item.quantity += 1

    cart_item.save()
    messages.success(request, 'Product added to your cart!')
    
    # Ensure that you always return an HttpResponse
    return redirect('cart_view')


def cart_view(request):
    user_id = request.session.get('user_id')  # Fetch the current user's ID from session
    cart_items = Cart.objects.filter(user_id=user_id)  # Get the items for the current user
    user_name = request.session.get('name', 'Guest')  # Fetch the user's name or use 'Guest'

    cart_data = []
    total_price = 0

    # Calculate total for each item and grand total
    for item in cart_items:
        item_total = item.product.price * item.quantity
        total_price += item_total
        cart_data.append({
            'product': item.product,
            'quantity': item.quantity,
            'price': item.product.price,
            'item_total': item_total,
        })

    # Pass both cart items and the user's name in the context
    context = {
        'cart_items': cart_data,
        'total_price': total_price,
        'user_name': user_name  # Pass the user_name to the template
    }
    
    return render(request, 'cart.html', context)