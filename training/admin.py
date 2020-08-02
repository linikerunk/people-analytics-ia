from django.contrib import admin
from .models import Training, Entity, Instructor, Event


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_name', 'category', 'training_type')


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('entity_name', 'social_reason', 'cnpj')


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('registro_instrutor', 'instructor_name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'value', 'event_date')
