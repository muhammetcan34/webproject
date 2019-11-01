from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class loginform(forms.Form):
    user_name = forms.CharField(max_length=100, label='kullanıcı adı')
    password = forms.CharField(max_length=100, label='parola',widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('kullanıcı adı veya şifre hatalı!')
        return super(loginform, self).clean()


class registerform(forms.ModelForm):
    user_name = forms.CharField(max_length=100, label='kullanıcı adı')
    password1 = forms.CharField(max_length=100, label='parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='parola doğrulama', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('parolalar eşleşmiyor!')
        return password2