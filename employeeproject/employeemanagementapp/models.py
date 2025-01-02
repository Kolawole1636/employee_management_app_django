from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=45)
    size = models.IntegerField()
    department_head = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.EmailField()
    salary = models.FloatField()
    tax = models.FloatField()
    balance = models.FloatField()
    departId = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.firstName

