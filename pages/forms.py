from dataclasses import field
from statistics import mode
from django import forms
from .models import UserInfo


class UserInterestForm(forms.ModelForm):
    # student_name = forms.CharField(max_length=200)
    # mail = forms.EmailField()


    class Meta:
        model = UserInfo
        fields = ['student_name', 'phone', 'mail', 'message']
    
# class ContactMailForm(forms.ModelForm):
    

    # class Meta:
    #     model = ContactUs
    #     fields = '__all__'