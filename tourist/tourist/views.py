from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

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
        return HttpResponseRedirect('thank-you/')  # Redirect to a thank you page
        
    return render(request, 'contact.html')

def thank_you(request):
    # Add any necessary logic here
    return render(request, 'thankyou.html')  # Assuming you have a template named 'thank_you.html'

