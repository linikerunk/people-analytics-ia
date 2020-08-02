from django.contrib import admin
from .models import Employee, CostCenter


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    pass
