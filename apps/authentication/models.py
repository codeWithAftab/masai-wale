# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

class Agent(models.Model):
    class Meta:
        unique_together=('mobile_no', 'email_id')
        
    name=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    email_id=models.EmailField(id=True, max_length=254)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    Bank_acc=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)