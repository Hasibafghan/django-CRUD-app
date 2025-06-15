from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , SetPasswordForm
from django import forms
from .models import Record

# we use widget tweaks to add bootstrap classes to the form fields
class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=30,label='First Name' , )
    last_name = forms.CharField(max_length=30,label='Last Name' , )
    email= forms.EmailField(max_length=30,label='Email', ) # widget=forms.TextInput(attrs={class:'form-control' , 'placeholder':'Enter your username' , 'name':'username'})
    username= forms.CharField(max_length=30,label='Username' , ) 
    password1 = forms.CharField(
        max_length=30,
        label='Password',
        # widget=forms.PasswordInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Password must be at least 8 characters',
        #     # 'name': 'password',
        #     # 'type': 'password'
        # })
    )
    password2 = forms.CharField(
        max_length=30,
        label='Confirm Password',
        # widget=forms.PasswordInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Re-enter password',
        #     # 'name': 'password',
        #     # 'type': 'password'
        # })
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken. Try another.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered, Try to login.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'username', 'password1', 'password2']



class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['created_at']

# class AddRecordForm(forms.ModelForm):
#     class Meta:
#         model = Record
#         exclude = []