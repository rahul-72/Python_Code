from django import forms

class Login(forms.Form):  #we are inheriting Form class of forms module
    email= forms.EmailField()
    password= forms.CharField(min_length=5, widget=forms.PasswordInput)


class Signup(forms.Form):
    email= forms.EmailField()
    password= forms.CharField(min_length=5, widget=forms.PasswordInput)
    fname= forms.CharField()
    lname= forms.CharField()