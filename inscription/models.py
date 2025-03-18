from django.db import models

class Inscription(models.Model):
    ecole = models.CharField(max_length=150)
    membre1 = models.CharField(max_length=150)
    classe1 = models.CharField(max_length=150)
    membre2 = models.CharField(max_length=150)
    classe2 = models.CharField(max_length=150)
    membre3 = models.CharField(max_length=150)
    classe3 = models.CharField(max_length=150)
    email = models.EmailField()
    theme = models.CharField(max_length=150)
    article = models.FileField(upload_to='article/')
    
    def __str__(self):
        return self.ecole
    
    