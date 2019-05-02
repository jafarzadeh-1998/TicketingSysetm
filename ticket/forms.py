
from django import forms

class login_form(forms.Form):
    # auto_id=False
    username = forms.CharField( max_length=100)
    password = forms.CharField( max_length=100)

class signup_form(forms.Form):
    auto_id=False
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class message_form(forms.Form):
    auto_id=False
    message = forms.CharField(max_length=100)