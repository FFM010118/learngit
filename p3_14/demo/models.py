from django.db import models

class Cls(models.Model):
    class_number = models.CharField(max_length=20)

class Stuendt(models.Model):
    stu_name = models.CharField(max_length=20)
    code = models.CharField(max_length=50)
    cls = models.ForeignKey(Cls,on_delete=models.CASCADE)
