from django.db import models


class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    designation = models.CharField(max_length=255)