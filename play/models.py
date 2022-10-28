from datetime import date
from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.

class docker_image(models.Model):

    name = models.CharField(max_length=200 , primary_key=True) 
    image = models.CharField(max_length=255)
    command = models.CharField(max_length=255 , null=True )
    created_at=models.DateField(auto_now_add=True)
    class Meta : 
        db_table= 'Image'

    def __str__(self) -> str:
        return self.name



class Enviroment_Vars(models.Model):
    images = models.ForeignKey(docker_image ,on_delete=models.CASCADE  ,db_index=True)
    key = models.CharField(max_length=200 , db_index=True)
    value = models.CharField(max_length=200 , db_index=True)
    class Meta : 
        db_table= 'Enviroment_Vars'
    def __str__(self) -> str:
        return self.key



class Container(models.Model):
        
    Running = 'R'
    Finished = 'F'
    Image_Status_Choises =[
        ('R' , 'Running'),
        ('F' , 'Finished')
    ]

    name = models.CharField(max_length=200)
    images = models.ForeignKey(docker_image ,on_delete=models.CASCADE)
    Status = models.CharField(max_length=1 , choices=Image_Status_Choises , default='F')

    class Meta : 
        db_table= 'Container'

class History(models.Model):
    Container_Name = models.CharField(max_length=200) 
    App_Name=models.CharField(max_length=200 ) 
    Image_Name=models.CharField(max_length=200 ) 
