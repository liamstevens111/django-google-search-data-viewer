from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import BaseUser

from django import forms

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        return self.cleaned_data['email'].lower()

class UserEditForm(UserChangeForm):
    class Meta:
        model = BaseUser
        fields = ('email', 'password',
                  'is_active', 'is_admin')


class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.EmailInput(attrs={'autofocus': 'True'})

    def clean_username(self):
        return self.cleaned_data['username'].lower()