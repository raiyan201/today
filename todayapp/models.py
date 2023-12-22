from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, unique=True, default=None)
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()
    

    def __str__(self):
        return self.emp_name
        