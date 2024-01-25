from django.db import models

class UserModel(models.Model):
    user = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.user}"
    
class UserProblem(models.Model):
    user = models.ForeignKey(UserModel, related_name='images', on_delete=models.CASCADE)
    description = models.TextField()
    images = models.ManyToManyField('UserProblemImage', related_name='user_problems', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class UserProblemImage(models.Model):
    image = models.ImageField(upload_to='user_problem_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)