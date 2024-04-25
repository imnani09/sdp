from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from django.db.models import Q
from .models import User,HotelBooking
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    return render(request, 'homepage.html')

def feedbackpage(request):
    return render(request, 'feedback.html')


def loginpage(request):
    return render(request, 'login.html')


def registerpage(request):
    return render(request, 'register.html')


def aboutpage(request):
    return render(request,'about.html')


def contactpage(request):
    return render(request,'contact.html')

def packagespage(request):
    return render(request,'packages.html')

def hotelspage(request):
    return render(request,'hotels.html')

def travelpage(request):
    return render(request,'travel.html')
 
def accomadationpage(request):
    return render(request,'accomadation.html')

def hotelspaymentpage(request):
    return render(request,'hotels_payment.html')

def paymentspage(request):
    return render(request,'payments.html')

def luxpage(request):
    return render(request,'lux_package.html')

def stndpage(request):
    return render(request,'stnd_package.html')

def delxpage(request):
    return render(request,'delx_package.html')

def transportationpage(request):
    return render(request,'transportation.html')

def registeruser(request):
    if request.method == 'POST':
        new_user = User(
            full_name=request.POST['fullName'],
            date_of_birth=request.POST['dob'],
            gender=request.POST['gender'],
            email=request.POST['email'],
            phone_number=request.POST['phone'],
            address=request.POST['address'],
            country=request.POST['country'],
            username=request.POST['username'],
            password=request.POST['password'],
            agreed_to_terms=request.POST['agreeTerms']
        )
        new_user.save()
        return redirect('homepage')
    

# def loginuser(request):
#     if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             flag = User.objects.filter(Q(username=username, password=password))  # feild name,local variable and class variable.        
#             if flag:
#                 # login(request,User)
#                 return redirect("homepage")       
#             else:
#                 return render(request, "loginfail.html")

def loginuser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user, backend='adminapp.backends.CustomUserBackend')
            return redirect('homepage')

     

    return render(request, 'loginfail.html')


def logout_the_page(request):
    logout(request)
    return redirect('homepage')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        subject = 'Contact Form Submission'
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        sender_email = settings.EMAIL_HOST_USER
        recipient_list = [sender_email]  # Change this to your recipient email address
        send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
        
        # Redirect after successful submission
        return redirect('thank_you')  # Redirect to a thank you page
        
    return render(request, 'contact.html')



from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

def hotel_booking(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        credit_card = request.POST.get('creditCard')
        expiry_date = request.POST.get('expiryDate')
        cvv = request.POST.get('cvv')

        # Save data to the database
        booking = HotelBooking.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            credit_card=credit_card,
            expiry_date=expiry_date,
            cvv=cvv
        )
        booking.save()

        # Redirect after successful submission
        return redirect('thank_you')  # Redirect to a thank you page

    return render(request, 'hotels_payment.html')

