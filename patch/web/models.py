from django.db import models


FAQ_TYPE = (
    ("rent_tracking","Rent Tracking"),
    ("new_deposite","New Deposite"),
    ("existing_deposite","Exisiting Deposite"),
)
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


class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    faq_type = models.CharField(max_length=255,choices=FAQ_TYPE)
    
    def __str__(self) -> str:
        return self.title