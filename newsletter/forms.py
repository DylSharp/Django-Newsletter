__author__ = 'Dylan'
from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # if not '.edu' in email:
        #     raise forms.ValidationError('Please use a valid edu email address')
        return email