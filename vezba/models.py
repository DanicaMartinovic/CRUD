from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=50)
    
    def __str__(self):
        return 'Student: {self.first_name} {self.last_name}'
    
    
