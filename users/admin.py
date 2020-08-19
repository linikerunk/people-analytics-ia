from django.contrib import admin
from .models import Employee, CostCenter, Unity


@admin.register(Unity)
class Unity(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ['number', 'name_department', 'responsible']
