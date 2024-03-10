from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    designation = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Promoter(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="promoters/")
    
    def __str__(self):
        return self.name
