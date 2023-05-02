from django import forms
from .models import Guest

class SignupForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["user","budget"]