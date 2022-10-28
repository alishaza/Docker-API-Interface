from dataclasses import field, fields
from pyexpat import model
from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from .models import Enviroment_Vars, History, docker_image , Container

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = docker_image
        fields= ['name' , 'image' , 'command' , 'created_at'  ]
   

class ContainerSerializer (serializers.ModelSerializer):
    images = serializers.StringRelatedField()
    class Meta:
        model = Container
        fields = ['name', 'Status' , 'images']

class variableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enviroment_Vars
        fields = ['key' , 'value']
    
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enviroment_Vars
        fields = ['key' , 'value' , 'images']
    images = ImageSerializer()

    def create(self, validated_data):
        data = Enviroment_Vars(**validated_data)

        return data
        

class dockerserializer(serializers.Serializer):
    name = serializers.CharField(max_length=255 )
    image = serializers.CharField(max_length=255)
    command = serializers.CharField(max_length=255)
    variables = serializers.ListField()


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields= ['Container_Name' , 'App_Name' , 'Image_Name']
