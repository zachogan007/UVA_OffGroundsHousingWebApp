from django import forms
from .models import UserInfo

class AccountForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ['year', 'phone_number', 'instagram']
