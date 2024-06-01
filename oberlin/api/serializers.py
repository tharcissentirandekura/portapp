#JSON data is converted to python data types and vice versa
from rest_framework import serializers
from .models import College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__' #returning all the fields of the model
        #fields = ['id','name', 'location'] #returning only the name and location fields of the model