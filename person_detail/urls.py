from django.urls import path,include
from .views import *
from person_detail import views





urlpatterns = [
    path('get', views.Display),
    path('post/',views.Post ),
    
    path('per',home.as_view()),
    path('perso/<int:pk>/', IndiviualDetail.as_view()),
    path('register/', RegistrationUser.as_view() ),
]
   
