from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import BaseUser
from .forms import UserSignUpForm, UserEditForm


class CustomUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserSignUpForm

    list_display = ('email', 'is_admin', 'is_active',
                    'is_staff', 'created_at', 'updated_at')

    list_filter = ('is_active', 'is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Booleans', {'fields': ('is_active', 'is_admin')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')
                        }
         )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ("created_at", "updated_at")

# Register your models here.
admin.site.register(BaseUser, CustomUserAdmin)
admin.site.unregister(Group)