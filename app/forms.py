from django import forms
from .models import Users



class User_form(forms.ModelForm):
    class Meta:
        models= Users
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }