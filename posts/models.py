from django.db import models


# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=1000)
    
    title = models.CharField(max_length=100)

    



    def __str__(self):
        return self.title

