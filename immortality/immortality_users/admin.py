from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import ImmortalityUser


class CustomUserAdmin(UserAdmin):
    """ some cookie-cutter model I found. Probably doesnt work"""
    # I'm not using forms
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = ImmortalityUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ImmortalityUser, CustomUserAdmin)
