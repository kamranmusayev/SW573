from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User_profile, Post


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
       


class Profile_EditForm(forms.ModelForm):
    form_control_attr = forms.TextInput(attrs={
            'class': 'form-control'
        })
    
    name = forms.CharField(widget=form_control_attr)     
    
    username = forms.CharField(widget=form_control_attr)
    email = forms.EmailField(widget=form_control_attr)
    bio = forms.CharField(widget=form_control_attr)
    class Meta:
        model = User_profile
        fields = ['name', 'username', 'email', 'bio']




class PostForm(forms.ModelForm):
    form_control_attr = forms.TextInput(attrs={
            'class': 'form-control'
        })

    title = forms.CharField(widget=form_control_attr)

    post_data = forms.CharField(widget=forms.Textarea())
    post_data.widget.attrs.update({"class": "form-control"})

    date = forms.DateField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }))
    

    place = forms.CharField(widget= form_control_attr)

    place.widget.attrs.update({"style": "margin-bottom: 2rem;"})

    class Meta:
        model = Post
        fields = ['title', 'post_data', 'date', 'place']