from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404

# model 1
class home(APIView):
    def get(self, request, format=None):
        auth = Author.objects.all()      
        serializer = AuthorSerializer(auth, many=True)
        return Response(serializer.data)
    
class BookList(APIView):
    def get(self, request, format=None):
        Books = Book.objects.all()
        serializer = BookatSerializer(Books, many=True)  # using custom serializer 
        return Response(serializer.data)
    
# model 2

class collegeList(APIView):
    def get(self, request, format=None):
        coll = College.objects.all()
        #serializer = College_nSerializer(coll, many=True) to use custom serlializers
        serializer = CollegeSerializer(coll, many=True)
        return Response(serializer.data)

class deparmentList(APIView):
    def get(self, request, format=None):
        depa = Department.objects.all()
        serializer = DepartmentSerializer(depa, many=True)
        return Response(serializer.data)

# pro -> dep
class professorList(APIView):
    def get(self, request, format=None):
        prof = Professor.objects.all()
        serializer = ProfessorSerializer(prof, many=True)
        return Response(serializer.data)


class libraryList(APIView):
    def get(self, request, format=None):
        lib = Library.objects.all()
        serializer = LibrarySerializer(lib, many=True)
        return Response(serializer.data)