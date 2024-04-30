from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# @api_view(['GET'])
# def home(request):
#     return Response({"message": "Hello, world!"})


# withou use id
class home(APIView):
    def get(self, request, format=None):
        books = Person.objects.all()      
        serializer = PersonSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
       # if request.data.exist():
       # if request.data["age"] < 18:  for any condition
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  # with use of id
class IndiviualDetail(APIView):

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = Person.objects.get(pk=pk)
        serializer =PersonSerializer(person)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        serializer =PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
       Person = self.get_object(pk)
       Person.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
        

class RegistrationUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({ 'status': 403  , 'errors' : serializer.errors, 'message' : 'something went worng'})
            
        serializer.save()

        user= User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        
        return Response({ 'status': 200  , 'payload' : serializer.data, 'token' : str(token_obj) , 'message' : 'your data is saved'})
        
      
    

def Display(request):
    return render(request, 'get.html')

def Post(request):
    return render(request,'post.html')