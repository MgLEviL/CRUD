from django.urls import path
from django.conf.urls import url
from CORE import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.addNewNote, name="addNewNote"),
    path('delete/', views.deleteNote, name="deleteNote"),
    path('update/', views.updateNote, name="updateNote"),
]