from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import BaseUser

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
    def clean_username(self):
        return self.cleaned_data['username'].lower()