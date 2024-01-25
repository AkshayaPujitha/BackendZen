from django.db import models

class UserModel(models.Model):
    user = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.user}"
    
