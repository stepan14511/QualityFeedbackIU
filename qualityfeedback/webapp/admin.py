from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Course, Group

class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email', 'is_admin', 'role', 'first_name', 'last_name')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Group)
