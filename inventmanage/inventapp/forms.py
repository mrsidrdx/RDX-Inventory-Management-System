from django import forms
from .models import (User, UserProfile, Customer, Inventory, Item, Orders, Payment)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('user_mobile', 'inv_id', 'users_id')
