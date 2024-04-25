from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    agreed_to_terms = models.CharField(max_length=10)

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        db_table = 'user_table'

class HotelBooking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    credit_card = models.CharField(max_length=16)  # Assuming credit card number is 16 digits
    expiry_date = models.CharField(max_length=5)  # Assuming expiry date format is MM/YY
    cvv = models.CharField(max_length=4)          # Assuming CVV is 3 or 4 digits
    
    def __str__(self):
        return self.full_name

