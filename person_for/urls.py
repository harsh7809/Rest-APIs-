from django.urls import path,include
from .views import *




urlpatterns = [
    path('aut',home.as_view()),
    #  path('books/<int:pk>/', BookDetail.as_view())
    path('boo/', BookList.as_view()),
    path('col/', collegeList.as_view()),
    path('dep/', deparmentList.as_view()),
    path('pro/', professorList.as_view()),
    path('lib/', libraryList.as_view()),

]
   
