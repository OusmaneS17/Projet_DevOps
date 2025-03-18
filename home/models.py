from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    email = models.EmailField()
    objet = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.nom

class Newsletter(models.Model):
     email = models.EmailField()

     def __str__(self):
        return self.email




  
