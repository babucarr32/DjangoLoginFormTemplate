from .models import loginModel
from django import forms

class loginForm(forms.ModelForm):
    class Meta:
        model = loginModel
        fields = ['email', 'password']
        widget = {
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }