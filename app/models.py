from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    choice_field = (
        ('Doctor','Doctor'),('Patient','Patient')
    )
    User_Type = models.CharField(max_length=20,choices=choice_field)
    image = models.ImageField(upload_to='media/')
    address = models.TextField(max_length=150)
    def __str__(self):
        return self.User_Type