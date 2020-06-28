from django.db import models

# Creae your models here.
class feedback(models.Model):
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    subject= models.CharField(max_length=200)
    message= models.CharField(max_length=200)
    class Meta:
        db_table="feedback"
    def __str__(self):
        return self.name   
        
class order(models.Model):
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    bag= models.CharField(max_length=200,default="")
    materialChecked2= models.CharField(max_length=200)
    instructions= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    bleachwhites= models.CharField(max_length=200)
    deliverydate= models.CharField(max_length=200,default="")
    description= models.CharField(max_length=200)
    item= models.CharField(max_length=200,default="")
    laundry= models.CharField(max_length=200,default="")
    pickupdate= models.CharField(max_length=200)
    class Meta:
        db_table="order"
    def __str__(self):
        return self.name   
        
class pricing(models.Model):
    product= models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    price= models.CharField(max_length=200)
    price2= models.CharField(max_length=200)
    class Meta:
        db_table="pricing"
    def __str__(self):
        return self.name  
        
        
class login(models.Model):
    email= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    class Meta:
        db_table="login"
    def __str__(self):
        return self.name   