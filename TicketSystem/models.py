from django.db import models

import TicketSystem

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
    num = models.IntegerField(default=150)      #航班可容纳人数
    num_a = models.IntegerField(default=150)      #票余量

class order(models.Model):
    O_Id = models.CharField(max_length=10,default='',primary_key=True)
    U_Id = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    F_Id = models.ForeignKey(FlightInfo,on_delete=models.CASCADE)
    status = models.BooleanField(default='0')   #判断是否付款
    seat = models.IntegerField(default=1)

class orderinfo(models.Model):
    O_Id = models.CharField(max_length=10,primary_key=True)
    seat = models.IntegerField()
    u_id = models.CharField(max_length=18)
    f_id = models.CharField(max_length=20)
    s_time = models.DateTimeField()
    a_time = models.DateTimeField()
    origin = models.CharField(max_length=20)
    des = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    status = models.BooleanField()
    
    class Meta:
        db_table = 'order_view'
        managed = False  # 将此处设置False 