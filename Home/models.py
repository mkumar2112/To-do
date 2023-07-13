from django.db import models
from django.contrib.auth.models import User



# Create your models here.

# Creating our Task model...
class To_do_List_model(models.Model):
    title = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']

# Creating our Contact model and save there fields.
class Contacts(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email_Name = models.CharField(max_length=254)
    Address_1 = models.CharField(max_length=500)
    Address_2 = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    State = models.CharField(max_length=500)
    Zip = models.CharField(max_length=500) 
    # Check = models.BooleanField()

    def __str__(self):
        return self.First_Name
    
