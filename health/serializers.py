from rest_framework import serializers
from .models import BodyMassIndex


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BodyMassIndex
        fields = ('identifier', 'weighing_date', 'weight', 'height',
                  'abdominal_circumference', 'systolic_blood_pressure',
                  'diastolic_blood_pressure', 'classification',
                  'classification_text', 'imc')