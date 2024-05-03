from django.db import models

# model structure = author -> review,book

class Author(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    

    def __str__(self):
        #return f"{self.name} - {self.book.title}" 
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books" , null=True, blank=True, default=None)
  
    def __str__(self):
        return self.title
    
class  Review(models.Model):
    rating = models.IntegerField(default=None)
    author= models.ForeignKey(Author, on_delete=models.CASCADE,related_name="ratings")



# model structure = college-> professor-> Professor

class College(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=100)
    college= models.ManyToManyField(College,related_name="departments")  

    def __str__(self):
        return self.name

class Professor(models.Model):
    name=models.CharField(max_length=100)
    department= models.ManyToManyField(Department,related_name="professors")

    def __str__(self):
        return self.name
    

class Library(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()


