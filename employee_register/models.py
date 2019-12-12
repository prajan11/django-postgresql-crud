from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    image = models.ImageField(upload_to='employee_images', blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.
       