from django import forms
from django.contrib.auth.models import User







class register_users(forms.Form):
    name = forms.CharField(max_length=444,widget=forms.TextInput(attrs={'placeholder':'your name'}))
    email = forms.EmailField(max_length=444,widget=forms.TextInput(attrs={'placeholder':'your email'}))
    password_1 = forms.CharField(max_length=444,widget=forms.TextInput(attrs={'placeholder':'password'}))
    password_2 = forms.CharField(max_length=444,widget=forms.TextInput(attrs={'placeholder':'again password'}))



    def clean_name(self):
        nam = self.cleaned_data['name']
        if User.objects.filter(username=nam).exists():
            raise forms.ValidationError('این نام از قبل وجود دارد')
        return nam

    def clean_email(self):
        ema = self.cleaned_data['email']
        if User.objects.filter(email=ema).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود دارد')
        return ema

    def clean_password_2(self):
        pas1 = self.cleaned_data['password_1']
        pas2 = self.cleaned_data['password_2']
        if pas1 != pas2:
            raise forms.ValidationError('پسورد ها با یکدیگر فرق دارند')
        elif len(pas1) < 5 > len(pas2) :
            raise forms.ValidationError('رمز باید بیشتر از 5 کلمه باشد')
        return pas2



class join_users(forms.Form):
    user_name = forms.CharField(max_length=444,widget=forms.TextInput(attrs={'placeholder':'enter username'}))
    user_password = forms.CharField(max_length=444,widget=forms.TextInput(attrs={'placeholder':'enter password'}))