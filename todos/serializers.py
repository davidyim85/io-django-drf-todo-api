from .models import Todo
from rest_framework import serializers

# serial and deserialize data (data = the data from the table ) to JSON
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    #for configuring the todoserializer from above
    class Meta:
        #the mode to serialize
        model=Todo
        #show all fields
        fields='__all__'