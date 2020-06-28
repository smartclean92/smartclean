from django import forms
from dryclean.models import feedback , order , pricing,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class feedbackform(forms.ModelForm):
    name= forms.CharField(max_length=200)
    phone= forms.CharField(max_length=200)
    email= forms.CharField(max_length=200)
    subject= forms.CharField(max_length=200)
    message= forms.CharField(max_length=200)
    class Meta:
        model=feedback
        fields="__all__"
        

class orderform(forms.ModelForm):
    name= forms.CharField(max_length=200)
    phone= forms.CharField(max_length=200)
    email= forms.CharField(max_length=200)
    bag= forms.CharField(max_length=200)
    materialChecked2= forms.CharField(max_length=200)
    instructions= forms.CharField(max_length=200)
    address= forms.CharField(max_length=200)
    bleachwhites= forms.CharField(max_length=200)
    deliverydate= forms.CharField(max_length=200)
    description= forms.CharField(max_length=200)
    item= forms.CharField(max_length=200)
    laundry= forms.CharField(max_length=200)
    pickupdate= forms.CharField(max_length=200)
    class Meta:
        model=order
        fields="__all__"
        
class pricingform(forms.ModelForm):
    product= forms.CharField(max_length=200)
    name= forms.CharField(max_length=200)
    price= forms.CharField(max_length=200)
    price2= forms.CharField(max_length=200) 
    class Meta:
        model=pricing
        fields="__all__"
        
class loginform(forms.ModelForm):
    email= forms.CharField(max_length=200)
    password= forms.CharField(max_length=200)
    class Meta:
        model=login
        fields="__all__"