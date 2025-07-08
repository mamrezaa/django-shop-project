

from django import forms


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput
        (attrs={'class':'form-control'}))
    
    count = forms.IntegerField(label='ایمیل',widget=forms.NumberInput(
        attrs={'class':'form-control', 'id':'input-quantity'}
    ),initial=1)