from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Owner(models.Model):
    username=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

class Blog(models.Model):
    author=models.ForeignKey(
        Owner,
        on_delete=models.CASCADE
    )
    heading=models.CharField(max_length=30,blank=False)
    date=models.DateField(auto_now_add=True)
    data=models.DataField(blank=True)

    


