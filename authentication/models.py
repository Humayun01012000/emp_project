from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank= True)


    def __str__(self):
        return f"{self.user.username} - {self.role.name}"