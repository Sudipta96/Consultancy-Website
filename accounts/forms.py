from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Account

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")
    fullname = forms.TextInput()

    class Meta:
        model = Account
        fields = ("fullname","username","email","password1", "password2", "gender", "contact_number")

    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError(f'Email {username} is already in use.')



class SignInForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'password',)


    def clean(self):
        if self.is_valid():
            print("valid...")
            email = self.cleaned_data['email'].lower()
            password = self.cleaned_data['password']
            try:
                inactive_user = Account.objects.get(email=email)
                if inactive_user and inactive_user.is_active is False:
                    raise forms.ValidationError("Your account has not activated yet. Please activate it to sign in.")
            except Account.DoesNotExist:
                raise forms.ValidationError("Invalid email address")
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password")

