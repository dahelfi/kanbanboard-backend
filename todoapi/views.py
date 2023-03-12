from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from todoapi.models import Todo, Contact
from todoapi.serializers import TodoSerializer, ContactSerializer
from datetime import datetime

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTodos(request):
    user = request.user
    todos = user.todo_set.all()
    serializer = TodoSerializer(todos, many = True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTodo(request, primaryKey):
    todo = Todo.objects.get(id= primaryKey)
    todo.delete()
    return Response('Todo was deleted!')


@api_view(['DELETE'])
def deleteContact(request, primaryKey):
    contact = Contact.objects.get(id= primaryKey)
    contact.delete()

    return Response('Contact was deleted')

@api_view(['PUT'])
def updateTodo(request, primaryKey):
    data = request.data
    todo = Todo.objects.get(id= primaryKey)
    serializer = TodoSerializer(instance = todo, data = data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTodo(request):
    data = request.data
    user = request.user
    todo = Todo.objects.create(
        author = user,
        name = data['name'],
        created_at = data['created_at'],
        description = data['description'],
        category = data['category'],
        priority = data['priority'],
        development_state = data['development_state'],
        expire_date = data['expire_date'],
    )
    todo.contacts.set(data['contacts'])

    serializer = TodoSerializer(todo, many = False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getContacts(request):
    user = request.user
    contacts = user.contact_set.all()
    serializer = ContactSerializer(contacts, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createContact(request):
    data = request.data
    user = request.user
    contact = Contact.objects.create(
        author = user,
        prename = data['prename'],
        lastname = data['lastname'],
        email = data['email'],
        phonenumber = data['phonenumber'],
        color = data['color']
    )

    serializer = ContactSerializer(contact, many = False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateContact(request, primaryKey):
    data = request.data
    contact = Contact.objects.get(id= primaryKey)
    serializer = ContactSerializer(instance = contact, data = data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

