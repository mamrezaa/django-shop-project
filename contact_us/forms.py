

from django import forms


class ContactUsForm(forms.Form):
    fullName = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    message = forms.CharField(label='پیام', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما'}))