from rest_framework import serializers
from onlineapp.models import *

class CollegeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    location = serializers.CharField(max_length=64)
    acronym = serializers.CharField(max_length=8)
    contact = serializers.EmailField()

    def create(self,validate_data):
        return College.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.location = validated_data.get('location',instance.location)
        instance.acronym = validated_data.get('acronym',instance.acronym)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.save()
        return instance

    # class Meta:
    #     model = College
    #     fields = ('name','location','acronym','contact')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','dob','email','db_folder','college','dropped_out')
