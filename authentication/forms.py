from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')