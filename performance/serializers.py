from rest_framework import serializers
from .models import Skill, Evaluation, EvaluationSkill


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name', 'description')


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluation
        fields = ('valuator', 'rated', 'year', 'skills')


class EvaluationSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = EvaluationSkill
        fields = ('evaluation', 'skill', 'grade')

