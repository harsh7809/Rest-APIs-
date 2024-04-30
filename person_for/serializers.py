from rest_framework import serializers
from .models import *
from datetime import timedelta


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']
   

class ReviewSerializer(serializers.ModelSerializer):
      class Meta:
        model = Review
        fields = ['rating'] 

class AuthorSerializer(serializers.ModelSerializer):
    ratings = ReviewSerializer(many=True, read_only=True) # link to author ratings
    books = BookSerializer(many=True, read_only=True)     # link  to author's books
    class Meta:
        model = Author
        fields = ['id', 'name','books','ratings']


# custom serializer (when model is connect with related name this method is used to exract parent data by calling child data )
       # methods in serializers
class BookatSerializer(serializers.ModelSerializer):
       author_name = serializers.SerializerMethodField()   

       class Meta:
         model = Book
         fields = ['title', 'author_name']

       def get_author_name(self, obj):
            return obj.author.name
        
       # this method is not useable doubt
# class Author_nSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = Author
#         fields = ['name']

# class BookatSerializer(serializers.ModelSerializer):
#        author = Author_nSerializer(many=True, read_only=True) 

#        class Meta:
#          model = Book
#          fields = ['title', 'author.name']

       
#model ->2

class  ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor                             
        fields = ['name']

 # it gives department -> professors
class DepartmentSerializer(serializers.ModelSerializer):
    professors=  ProfessorSerializer(many=True,read_only=True)  
    class Meta:
        model = Department
        fields = ['name','professors'] 
        

    # it gives  college -> department -> professors
class CollegeSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = College
        fields = ('name', 'departments')


  # custom serializer to extract college-> department
class Department_nSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']
        
class College_nSerializer(serializers.ModelSerializer):
    departments = Department_nSerializer(many=True, read_only=True)
    class Meta:
        model = College
        fields = ('name', 'departments')


# extracting parent table data from child table (opposite)

   # professor -> department
class ProfessorSerializer(serializers.ModelSerializer):
    department = Department_nSerializer(many=True, read_only=True)
    class Meta:
        model = Professor                             
        fields = ['name','department']
     
        
# second method depth

# class ProfessorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Professor                             
#         fields = ['name','department'] 
#         depth = 1 for department
#       # depth = 2  department , college
        


# extra method in serializers
        

class LibrarySerializer(serializers.ModelSerializer):
    date_new=  serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = ['name','date','date_new']    # date_new is a new filed

    def get_date_new(self,obj):
        return  obj.date + timedelta(days=7)   

    
    




    
