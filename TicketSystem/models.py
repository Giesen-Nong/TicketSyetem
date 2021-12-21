from django.db import models

class UserInfo(models.Model):
    U_Id = models.CharField(max_length=18,primary_key=True)
    U_Name = models.CharField(max_length=10)
    U_password = models.CharField(max_length=30,default='123456')

class Airlines(models.Model):
    A_Name = models.CharField(max_length=20, primary_key=True)
    A_tel = models.CharField(max_length=11)


class FlightInfo(models.Model):
    A_Name = models.ForeignKey(Airlines,on_delete=models.CASCADE,default='')
    F_ID = models.CharField(max_length=20,primary_key=True)
    StartTime = models.DateTimeField()
    ArriveTime = models.DateTimeField()
    Origin = models.CharField(max_length=20)
    Destination = models.CharField(max_length=20)
    Price = models.CharField(max_length=10,default='')