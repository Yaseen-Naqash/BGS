from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator #NOTe
# When working directly with the model, make sure to call the model full_clean
# method before saving the model in order to trigger the validators. 
#This is not required when using ModelForm since the forms will do that automatically.


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=13,null=True)
    img = models.ImageField(default="default_profile.png")
    rating = models.DecimalField(max_digits=3, decimal_places=2,default=0.00)
    sells = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)
    archive = models.ManyToManyField('Boardgame',related_name='archive',blank=True)
    forSale = models.ManyToManyField('Boardgame',related_name='forsale',blank=True)
    wishList = models.ManyToManyField('Boardgame',related_name='wishlist',blank=True)

    
    def __str__(self) -> str:
        return self.username

class Deal(models.Model):

    STATUS = [
        ('0','OPEN DEAL'),
        ('1','SOLD'),
        ('2','SEMI SOLD'),
        ('3','UNKNOWN'),
    ]
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(max_length=1500,null=True,blank=True)
    #if i delete related name from these two field ill get reverse accessor erreor
    seller = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='seller')
    buyer = models.ManyToManyField(User,related_name='buyer',null=True,blank=True)
    stock = models.ManyToManyField('Boardgame',related_name='stock',null=True,blank=True)
    totalPrice = models.IntegerField(default=0,validators=[
            MaxValueValidator(100000000),
            MinValueValidator(50000),
        ])
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dealDate = models.DateField(null=True,blank=True)
    status = models.CharField(default=0,max_length=1,choices=STATUS)
    sellerToughts = models.TextField(max_length=500,null=True,blank=True)
    buyerToughts = models.TextField(max_length=500,null=True,blank=True)

    class Meta:
        ordering = ['-updated','-created']

    
    def __str__(self) -> str:
        return self.title
    

class Boardgame(models.Model):

    MADE_IN = [
        ('0','IRANI'),
        ('1','KHAREJI'),
        
    ]


    name = models.CharField(max_length=200,null=True)
    price = models.IntegerField(null=True,validators=[
            MaxValueValidator(100000000),
            MinValueValidator(10000),
        ])
    description = models.TextField(max_length=1500,null=True,blank=True) 
    made = models.CharField(default=0,max_length=1,choices=MADE_IN)
    topics = models.ManyToManyField('Topic',related_name='topics',null=True,blank=True)
    rank = models.IntegerField(null=True,blank=True,validators=[
            MaxValueValidator(5000),
            MinValueValidator(1),
        ])
    players = models.CharField(max_length=10,blank=True,null=True)
    duration = models.IntegerField(null=True,blank=True,validators=[
            MaxValueValidator(600),
            MinValueValidator(1),
        ])
    complexity = models.DecimalField(max_digits=3, decimal_places=2,null=True,blank=True)
    designer = models.CharField(max_length=100,null=True,blank=True)
    publisher = models.CharField(max_length=100,null=True,blank=True)
    publisher = models.CharField(max_length=100,null=True,blank=True)

    
    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200,null=True)
    

    def __str__(self) -> str:
        return self.name
    
    
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
