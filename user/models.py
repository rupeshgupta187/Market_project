from django.db import models

# Create your models here.

class mcategory(models.Model):
    Name=models.CharField(max_length=20)
    CPic=models.ImageField(upload_to='static/category/',default="")
    def __str__(self):
        return self.Name
class maincategory(models.Model):
    Name=models.CharField(max_length=20)
    Mpic=models.ImageField(upload_to='static/mcategory/',default="")
    def __str__(self):
        return self.Name


class Product(models.Model):
    pname=models.CharField(max_length=100)
    pprice=models.CharField(max_length=15)
    dprice=models.CharField(max_length=15)
    date=models.DateField()
    delivery=models.CharField(max_length=20)
    pcolor=models.CharField(max_length=15)
    pimage=models.ImageField(upload_to="static/product",default=True)
    pdesc=models.TextField()
    pcategory=models.ForeignKey(mcategory,on_delete=models.CASCADE, null=True)
    macategory=models.ForeignKey(maincategory,on_delete=models.CASCADE,null=True)


    # def __str__(self):
    #     return self.pname
    
class register(models.Model):
    Name=models.CharField(max_length=25)
    Address=models.CharField(max_length=25)
    Mob=models.IntegerField()
    Email=models.EmailField(max_length=25,primary_key=True)
    Password=models.IntegerField()
    def __str__(self):
        return self.Name