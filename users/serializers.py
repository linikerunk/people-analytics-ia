from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Employee, CostCenter, Unity


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


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
