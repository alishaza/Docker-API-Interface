from ast import Delete
import collections
from distutils.cmd import Command
from email.mime import image
import imp
from itertools import product
import random
import re
from sys import stderr, stdout
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from .ssh import ssh
from .models import Container, Enviroment_Vars, History, docker_image 
from .serializers import  BaseSerializer, HistorySerializer, ImageSerializer , ContainerSerializer, dockerserializer, variableSerializer
from play import serializers



# start a new container on /apps/run/<appname>
class container(APIView):
    def get(self , request , appname ) :        
        Image = docker_image.objects.get(pk=appname)
        serializer = ImageSerializer(Image)
        imagename= serializer.data['image']
        command = serializer.data['command']
        containername = random.randint(1001,1999)

        variables = Enviroment_Vars.objects.filter(images__name=imagename)
        serializer= variableSerializer(variables , many=True)
        
        vars=''
        for i in  list(serializer.data):
            key=list(i.items())[0][1]
            value =list(i.items())[1][1]
            vars+='-e {}:{} '.format(key,value)
        
        Docker_command = 'docker run -d {} --name {} {} {}'.format(vars,containername , imagename , command , serializer.data)
        output= ssh(Docker_command)
        
        container = Container()
        container.name = containername
        container.Status='R'
        container.images=Image
        container.save()

        history = History()
        history.Image_Name=imagename
        history.Container_Name=containername
        history.App_Name=appname
        history.save()

        return Response((' Command : {}').format(Docker_command) , status = status.HTTP_201_CREATED)

        


#/apps/<Image>
class app_detail(APIView):
    def get(self , request , name):
        Image = docker_image.objects.get(pk=name)
        serializer = ImageSerializer(Image)
        return  Response(serializer.data)
    def put(self , request , name):
        Image = docker_image.objects.get(pk=name)
        serializer= ImageSerializer(Image  , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,name):
        images = docker_image.objects.get(pk=name)
        images.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#view & add
#/apps         
class app_all_detail(APIView):
    def get(self , request):
        images = docker_image.objects.all()
        serializer = ImageSerializer(images , many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = dockerserializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        NewImage = docker_image()
        NewImage.name=serializer.data['name']
        NewImage.image=serializer.data['image']
        NewImage.command=serializer.data['command']
        NewImage.save()

        for index in serializer.data['variables']:
            for key , value in index.items():
                NewVariable = Enviroment_Vars()
                NewVariable.key=key
                NewVariable.value = value
                NewVariable.images=NewImage
                NewVariable.save() 
                #print(key , value)

        return Response(serializer.data  , status = status.HTTP_201_CREATED)
            


class Overall_ContainerStatus(APIView):
#view
# /apps/containers
    def get(self , request):
        containers = Container.objects.select_related('images').all()
        serializer = ContainerSerializer(containers , many=True)
        command = "docker ps | sed -rn 's/.* ([0-9]+$)/\\1/p' "
        ssh_stdout=ssh(command)
        ssh_stdout_lines=''
        for index in ssh_stdout:
            ssh_stdout_lines+=index

        for container in serializer.data:
            containername=container['name']     
            if containername in ssh_stdout_lines :
                container['Status'] = 'R'  
                temp =Container.objects.filter(name=containername).first()
                updated=ContainerSerializer(temp , data = container)  
                updated.is_valid(raise_exception=True)
                updated.save()
      
            else :
                container['Status'] = 'F'
                temp =Container.objects.filter(name=containername).first()
                updated=ContainerSerializer(temp , data = container)  
                updated.is_valid(raise_exception=True)
                updated.save()


        return Response(serializer.data)



class Specific_Container_Status(APIView):
    def get(self, request , imagename):
        containers = Container.objects.filter(images__name=imagename)
        serializer = ContainerSerializer(containers , many=True)
        command = "docker ps | sed -rn 's/.* ([0-9]+$)/\\1/p' "
        ssh_stdout=ssh(command)
        ssh_stdout_lines=''
        for index in ssh_stdout:
            ssh_stdout_lines+=index

        for container in serializer.data:
            containername=container['name']     
            if containername in ssh_stdout_lines :
                container['Status'] = 'R'  
                temp =Container.objects.filter(name=containername).first()
                updated=ContainerSerializer(temp , data = container)  
                updated.is_valid(raise_exception=True)
                updated.save()
      
            else :
                container['Status'] = 'F'
                temp =Container.objects.filter(name=containername).first()
                updated=ContainerSerializer(temp , data = container)  
                updated.is_valid(raise_exception=True)
                updated.save()
        return Response(serializer.data)