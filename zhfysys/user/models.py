from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    real_name = models.CharField(max_length=50)
    id_card_num = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.user_name
