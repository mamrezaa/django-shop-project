

from django import forms


class UserEdiProfileForm(forms.Form):
    
    first_name = forms.CharField(label="نام",widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'نام'}))
    
    last_name = forms.CharField(label="نام خانوادگی",widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'نام خانوادگی'}))