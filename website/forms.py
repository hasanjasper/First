from django import forms
from django.contrib.auth.models import *
from .models import *












class create_profile_users(forms.ModelForm):
    class Meta:
        model = Profile_website_users

        fields = ['fake_name','age','image','body']

        widgets = {


            'body' : forms.Textarea(attrs={'class':'form_control'}),
            'age'  : forms.TextInput(attrs={'class':'form_control'}),
            'fake_name'  : forms.TextInput(attrs={'class':'form_control'})

        }








class update_profile_users(forms.ModelForm):
    class Meta:
        model = Profile_website_users

        fields = ['fake_name','age','image','body']

        widgets = {


            'body' : forms.Textarea(attrs={'class':'form_control'}),
            'age'  : forms.TextInput(attrs={'class':'form_control'}),
            'fake_name'  : forms.TextInput(attrs={'class':'form_control'})

        }







class Add_commenter(forms.ModelForm):
    class Meta:
        model = Comment_users_post
        fields  = ['text_body']


        widgets = {
            'text_body' : forms.Textarea(attrs={'class':'form_control'})
        }


















