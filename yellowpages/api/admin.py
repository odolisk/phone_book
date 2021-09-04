from django.contrib import admin
from .models import Employee, Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'description')
    search_fields = ('name',)
    ordering = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'surname', 'name', 'middlename',
                    'position')
    search_fields = ('surname', 'name', 'middlename',)
    ordering = ('surname', 'name',)


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Employee, EmployeeAdmin)
