from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BaseUser

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('email', 'password1', 'password2')


class UserEditForm(UserChangeForm):
    class Meta:
        model = BaseUser
        fields = ('email', 'password',
                  'is_active', 'is_admin')