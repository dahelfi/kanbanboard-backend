from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getTodos/', views.getTodos, name="getTodos"),
    path('createTodo/', views.createTodo, name="createTodo"),
    path('<str:primaryKey>/updateTodo/', views.updateTodo, name="updateTodo"),
    path('<str:primaryKey>/deleteTodo/', views.deleteTodo, name="deleteTodo"),
    path('getContacts/', views.getContacts, name="getContacts"),
    path('createContact/', views.createContact, name="createContact"),
    path('<str:primaryKey>/updateContact/', views.updateContact, name="updateContact"),
    path('<str:primaryKey>/deleteContact/', views.deleteContact, name="deleteContact"),
]
