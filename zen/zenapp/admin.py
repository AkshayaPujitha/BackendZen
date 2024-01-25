from django.contrib import admin
from .models import UserModel,UserProblem,UserProblemImage
# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserProblemImage)
admin.site.register(UserProblem)

