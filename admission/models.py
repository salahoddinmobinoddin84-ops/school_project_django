from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    address = models.TextField()
    marksheet = models.FileField(upload_to='documents/')
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.full_name