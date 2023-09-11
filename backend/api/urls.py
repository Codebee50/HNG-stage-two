from django.urls import path
from . import views

urlpatterns =[
    path('', views.PersonView.as_view()),
    path('<str:pk>', views.PersonView.as_view())    
]