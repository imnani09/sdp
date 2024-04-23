from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'full_name', 'gender', 'date_of_birth', 'phone_number', 'country', 'agreed_to_terms')
    search_fields = ('username', 'email', 'full_name', 'phone_number', 'address', 'country')
    list_filter = ('gender',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'date_of_birth', 'gender', 'email', 'phone_number', 'address', 'country')}),
        ('Terms & Conditions', {'fields': ('agreed_to_terms',)}),
    )

admin.site.register(User, CustomUserAdmin)
