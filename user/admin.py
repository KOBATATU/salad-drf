from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(DefaultUserAdmin):
    form = CustomUserChangeForm
    add_form = DefaultUserAdmin.add_form
    model = User
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('location', 'birth_date')}),
    )

admin.site.register(User,CustomUserAdmin)