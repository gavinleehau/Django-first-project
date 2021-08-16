from __future__ import unicode_literals
from functools import update_wrapper
from django import db
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.expressions import OrderBy
from django.contrib.auth.models import User
import datetime



class Reporter(models.Model):
    first_name = models.CharField("Họ",max_length=30)
    last_name = models.CharField("Tên",max_length=30)
    email = models.EmailField("Địa chỉ Email")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    class Meta:
        db_table = "Reporter"

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    date =models.DateTimeField(auto_now_add=True)
    # image= models.ImageField(null=True, blank=True)
    # height_filed = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    
    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
        db_table = "Article"







# Create your models here.
# class Python2104(models.Model):
#     ten = models.CharField(max_length=150)
#     tuoi = models.IntegerField()
#     diachi = models.TextField()
#     class Meta:
#         db_table = "Python2104"

# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)

#     def __str__(self):
#         return "%s the place" % self.name
#     class Meta:
#         db_table = "Place"

# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s the restaurant" % self.place.name
#     class Meta:
#         db_table = "Restaurant"



# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['title']
#         db_table = "Publication"

#     def __str__(self):
#         return self.title

# class baiBao(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)
    
#     class Meta:
#         ordering = ['headline']
#         db_table = "baiBao"

#     def __str__(self):
#         return self.headline
    

# class Post(models.Model):
#     title = models.CharField(max_length=120)
#     content = models.TextField()
#     date =models.DateTimeField(auto_now_add=True)
#     # timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
#     image= models.ImageField(null = True)

#     # def __unicode__(self):
#     #     return self.title
#     def __str__(self):
#         return self.title
#     # class Meta:
#     #     db_table = "Post"

        


