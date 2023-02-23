# One-to-One Relationship
''' A one-to-one relationship means one record of a table is associated with exactly one record of another table '''
'''

A real-life example of a one-to-one relationship can be a country and its capital city. Each country has only one capital city. And each capital city is the capital city of only one country '''

from django.db import models

# The model Country
class Country(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
        return str(self.name)

# The model Capital 
class Capital(models.Model):
  country = models.OneToOneField(
        Country,
        on_delete=models.CASCADE,
        primary_key=True,
    )
  
  name = models.CharField(max_length=50)
  
  def __str__(self):
        return str(self.name)


'''
Django authentication has a default model User. Suppose you are building an e-commerce platform and want to extend your Customer model from User. You will do something like the following:

'''


from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
           User, 
           on_delete=models.CASCADE, 
           null=True, blank=True
    )
    
    name = models.CharField(max_length=256, null=True)
    email = models.EmailField(max_length=256, null=True)

    def __str__(self):
        return str(self.name)