from django.contrib import admin
from .models import BodyMassIndex

@admin.register(BodyMassIndex)
class BodyMassIndex(admin.ModelAdmin):
    list_display = ['identifier', 'get_name', 'imc', 'classification',
                    'classification_text']

    def get_name(self, obj):
        return obj.identifier.name
    get_name.short_description = 'Employee Name'