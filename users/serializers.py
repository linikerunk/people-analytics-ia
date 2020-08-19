from rest_framework import serializers
from .models import Employee, CostCenter, Unity


class UnitySerializer(serializers.ModelSerializer):
    model = Unity
    fields = ('name')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('identifier', 'name', 'admission', 'email', 'role', 
                  'resignation', 'birth_date', 'zip_code', 'phone', 'cpf',
                  'cost_center', 'gender', 'photo')


class CostCenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CostCenter
        fields = ('number', 'name_department', 'responsible')
