from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    class Meta:
        db_table = "login"