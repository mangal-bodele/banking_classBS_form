from django.db import models

class Banking(models.Model):
    MODE = [('C','Cash'),('O','Online')]
    fname = models.CharField(max_length=10 ,verbose_name='first name')
    lname = models.CharField(max_length=10, verbose_name='last name')
    mobile_number = models.IntegerField()
    dob = models.DateField(verbose_name='date of birth')
    acoount_number = models.CharField(max_length=20)
    branch_code = models.CharField(max_length=10,verbose_name='IFSC CODE')
    branch_name = models.CharField(max_length=10)
    address = models.CharField(max_length=20)