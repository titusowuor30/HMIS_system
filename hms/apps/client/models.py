from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=255)

    def __str__(self):
        return self.title
