from django.db import models

# Create your models here.
class student(models.Model):
    u_id = models.CharField(max_length = 100)
    name = models.CharField(max_length = 1000)
    file = models.ImageField(upload_to = 'media')
    points = models.IntegerField()

    def __str__(self):
        return self.u_id
    