from django.db import models

class Counter(models.Model):
    id = models.BigAutoField(primary_key=True)  # Ajout explicite de la clé primaire
    key = models.CharField(max_length=10)
    value = models.IntegerField()
