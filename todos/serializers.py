from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User

# serial and deserialize data (data = the data from the table ) to JSON
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #for configuring the todoserializer from above
    class Meta:
        #the mode to serialize
        model=Todo
        #show all fields
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user