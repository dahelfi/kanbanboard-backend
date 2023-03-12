from rest_framework.serializers import ModelSerializer
from todoapi.models import Todo, Contact

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta: 
        model = Contact
        fields = '__all__'