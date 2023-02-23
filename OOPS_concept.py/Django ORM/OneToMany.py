# One-to-Many Relationship
'''In a one-to-many relationship, one record of a table can be associated with one or more records of another table.'''

'''Again we can return to the example of a country. Consider the relationship between a country and its cities. A country has multiple cities. On the other hand, each city is in only one country. So it is a one-to-many relationship between a country and its cities'''


"""
a country can have many cities, and each city belongs to only one country.
To define a one-to-many relationship in Django models, we need to use the keyword ForeignKey."""

from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
        return str(self.name)
    
class City(models.Model):
  country = models.ForeignKey(
          Country, 
          on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  
  def __str__(self):
        return str(self.name)


'''In this one-to-many relationship, Country is the parent and City is the child.

Now let’s get back to our e-commerce example. We created a one-to-one relationship between the User model and the Customer model. A customer will place orders on an e-commerce platform. What will be the relationship between the Order model and the Customer model? A customer can place many orders but an order will be associated with only one customer. This creates a one-to-many relationship between Customer and Order.
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

      
class Order(models.Model):
    customer = models.ForeignKey(
            Customer, 
            on_delete=models.SET_NULL, 
            null=True, 
            blank=True
    )
    
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=256, null=True)

    def __str__(self):
        return str(self.id)