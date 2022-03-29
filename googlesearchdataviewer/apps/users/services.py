from typing import Optional
from .models import BaseUser

from googlesearchdataviewer.apps.profiles.models import Profile

def user_create(*, email: str, is_active: bool = True, is_admin: bool = False, password: Optional[str] = None) -> BaseUser:
    user = BaseUser.objects.create_user(
        email=email, is_active=is_active, is_admin=is_admin, password=password)
    
    Profile.objects.create(user=user)

    return user
