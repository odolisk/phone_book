from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Employee, Organization, User


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'description',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('author', )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'surname', 'name', 'middlename',
                    'position', 'personal_phone', 'work_phone', 'fax')
    search_fields = ('surname', 'name', 'middlename',)
    ordering = ('surname', 'name',)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', )}),
    ) + BaseUserAdmin.add_fieldsets
    search_fields = ('email',)
    ordering = ('email',)


admin.site.unregister(Group)
