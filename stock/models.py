from django.db import models
# from django.contrib.auth import registration
# User = registration()

class register(models.Model):
    
    
    customer_id=models.CharField(max_length=50)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=50)
  

class Product1(models.Model):
    
    Date = models.DateField()
    Product_No=models.IntegerField()
    Product_Name=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Cost_Price=models.IntegerField()
    Tot_Cost_Price=models.IntegerField()
    Selling_Price=models.IntegerField()
    Tot_selling_Price=models.IntegerField()
    
    class meta:
        db_table="Product1"

class order1(models.Model):
    
    Order_Date = models.DateField()
    Product_No=models.IntegerField()
    customer_id=models.CharField(max_length=50)
    Product_Name=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Selling_Price=models.IntegerField()
    Delivery_Date=models.DateField()
    Total=models.IntegerField()
    
    
    class meta:
        db_table="order"

class availableproduct(models.Model):
    
    Product_No=models.IntegerField()
    Product_Name=models.CharField(max_length=50)
    Quantity=models.IntegerField()

    class meta:
        db_table="availableproduct"

# Create your models here.
