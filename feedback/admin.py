from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from .models import Employee, Company, Feedback
from .forms import UserCreationForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    add_form = UserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('email', 'password1', 'password2')}
    ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Company)
admin.site.register(Feedback)
admin.site.register(Employee,UserAdmin)