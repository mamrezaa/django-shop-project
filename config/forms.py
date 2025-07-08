

from django import forms

from django.contrib.auth import get_user_model
from profiles.models import UserProfile
from django.core import validators



class Login_form(forms.Form):
    userName = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'userName'}))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'password'}
    ))


User = get_user_model()
class Register_form(forms.Form):
    userName = forms.CharField(label="نام کاربری",widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'نام کاربری'}),
         validators = [
             validators.MaxLengthValidator(limit_value=20,message='نام کاربری نباید بیش از 20 کاراکتر باشد !')
         ]
         )
    
    firstName = forms.CharField(label="نام",widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'نام'}))
    
    lastName = forms.CharField(label="نام خانوادگی",widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'نام خانوادگی'}))
    
    email = forms.EmailField(label="آدرس ایمیل",widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'آدرس ایمیل'}
    ),
    validators=[
        validators.EmailValidator('ایمیل نامعتبر است !')
    ]
    )

    
    phone_number = forms.CharField(
        label="شماره تلفن",
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'مثال: 09121234567',
            'type': 'tel'
        }),
        required=True
    )

    
    password = forms.CharField(label="رمز عبور",widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'رمز عبور'}
    ))

    password2 = forms.CharField(label='تکرار رمز عبور',widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'تکرار رمز عبور'}
    ))
    

    def clean_username(self):
        userName = self.cleaned_data.get('userName')
        query = User.objects.filter(username=userName)
        if query.exists():
            raise forms.ValidationError('this username is not available')
        
        return userName

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email)
        if query.exists():
            raise forms.ValidationError('this email is not available')
        
        return email

    def clean(self):
        data =  self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2 :
            raise forms.ValidationError('passwords do not match')
        
        return data
    

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        query = UserProfile.objects.filter(phone_number=phone_number)

        if not phone_number:
            return phone_number
        
        if query.exists():
            raise forms.ValidationError('this phone_number is not available')
        
        return phone_number
        