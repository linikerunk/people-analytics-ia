from django.contrib import admin

from . import models


class EvaluationSkillInline(admin.TabularInline):
    model = models.EvaluationSkill
    extra = 1


@admin.register(models.Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    inlines = [EvaluationSkillInline]
    list_display = ['__str__', 'average']

    def get_readonly_fields(self, request, obj):
        fields = ['created', 'modified']

        if obj:
            fields.insert(0, 'average')

        return fields


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    pass