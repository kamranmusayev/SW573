from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):

    form_control_attr = forms.TextInput(attrs={
            'class': 'form-control'
        })
    email = forms.EmailField(widget=form_control_attr)
    first_name = forms.CharField(widget=form_control_attr)
    last_name = forms.CharField(widget=form_control_attr)
    username = forms.CharField(widget=form_control_attr)

    password1 = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
        }), label='Password:')
    password2 = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
        }), label='Confirmation Password:')

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
       