from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from googlesearchdataviewer.apps.common.models import BaseModel


class BaseUserManager(BaseUserManager):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    class Meta:
        verbose_name = 'User'

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
