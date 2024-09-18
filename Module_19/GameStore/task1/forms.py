from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label="Введите логин")
#   password = forms.CharField(min_length=8,  required=True, label="Введите пароль")
#    repeat_password = forms.CharField(min_length=8,  required=True, label="Повторите пароль")
    age = forms.IntegerField(min_value=0,  max_value=120, required=True,label="Введите свой возраст")