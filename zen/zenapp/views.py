from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny


def home(request):
    return HttpResponse("hello world")


class UserModelView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    def create(self, request, *args, **kwargs):
        # Retrieve Firebase user ID from the request
        user_id = self.kwargs.get('user_id',None)
        print(self.kwargs)
        #print(request.query_params.get('user_id'))
        print(user_id)
        if user_id:
            # Check if the user ID already exists in the database
            user_identifier, created = UserModel.objects.get_or_create(user=user_id)

            if created:
                return Response({"detail": "User ID created successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "User ID already exists."}, status=status.HTTP_200_OK)

        return Response({"detail": "Firebase user ID not found in the request."}, status=status.HTTP_400_BAD_REQUEST)



