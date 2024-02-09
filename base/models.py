from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=13,null=True)
    img = models.ImageField(default="default_profile.png")
    #rating = 
    #sells = 
    #purchases = 
    #archive = ['objects']
    #forSale = ['objects']
    #wishList = ['objects']

class Deal(models.Model):
    #seller = 
    #buyer = 
    #stock = ['objects']
    #totalPrice = 
    #created = 
    #dealDate = 
    #status = 
    #sellerToughts = 
    #buyerToughts = 
    pass

class Boardgame(models.Model):
    #name = 
    #price = 
    #description = 
    #category = 
    #rank = 
    #minPlayer = 
    #maxPlayer = 
    #duration = 
    #weight = 
    #designer = 
    #publisher = 
    #artist = 
    pass

class Topic(models.Model):
    #name = 
    pass
    
class Room(models.Model):
    #host = 
    #topic = 
    #name = 
    #description = 
    #participants = 
    #updated = 
    #created = 
    pass

class Comments(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    #body = models.TextField()
    #updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)
    pass
