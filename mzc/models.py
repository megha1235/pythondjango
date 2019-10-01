from django.db import models

# Create your models here.
GENDER_CHOICES=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHER')
)
class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField(max_length=100)
    course=models.CharField(max_length=20)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default='M')

class Faculty(models.Model):
    name=models.CharField(max_length=30)
    designation=models.TextField(max_length=100)
    course=models.CharField(max_length=20)