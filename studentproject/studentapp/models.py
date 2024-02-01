from django.db import models

# Create your models here.

class stud_det(models.Model):
    Register_Number = models.IntegerField()
    Name = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    Branch = models.CharField(max_length=20)
    college_Name = models.CharField(max_length=20)
    College_Location = models.CharField(max_length=20)
    

class stud_fee(models.Model):
    Register_Number = models.IntegerField()
    Name = models.CharField(max_length=20)
    College_Fees = models.IntegerField()
    Bus_Fees = models.IntegerField()
    Exam_Fees = models.IntegerField()
    Total_Fees = models.IntegerField()
