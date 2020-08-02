from rest_framework import serializers
from .models import Training, Entity, Instructor, Event


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = ('training_name', 'category', 'content', 'required',
                  'resource', 'training_type', 'local', 'workload')


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = ('entity_name', 'social_reason', 'cnpj', 'sap_code',
                  'contact_person', 'phone', 'zip_code', 'address',
                  'city', 'state', 'email')


class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = ('registro_instrutor', 'instructor_name', 'instructor_photo',
                  'training')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('event_name', 'value', 'event_date', 'present_link',
                  'training', 'entity', 'instructor')
