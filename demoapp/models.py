from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_donmngmt = models.BooleanField(default=False)
    is_recipient = models.BooleanField(default=False)
    is_branchmngmt = models.BooleanField(default=False)


class user(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    aadhar_number = models.CharField(max_length=12,unique=True, validators=[MinLengthValidator(12)])
    phone = models.IntegerField(null=True,blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class donmngmt(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user


class recipient(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE,primary_key=True,related_name='Recipient')
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class branchmngmt(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE ,primary_key=True, related_name='branch')
    branchname = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class donation(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    medicine = models.CharField(max_length=100,null=True, blank=True)
    medicine_amount = models.IntegerField(null=True, blank=True)
    cash = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class requestdonation(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    medicine = models.CharField(max_length=100,null=True, blank=True)
    medicine_amount = models.IntegerField(null=True, blank=True)
    cash = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.user