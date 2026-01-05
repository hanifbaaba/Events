
from rest_framework import serializers
from .models import Events

class EventsSerializer(serializers.ModelSerializer):

    # user = serializers.ReadOnlyField(source='user.id')
    # photo_of_event = serializers.ImageField(required=False, allow_null=True)


    class Meta:
        model = Events
        fields = '__all__'
        # read_only_fields = ['user', 'created_at', 'updated_at',]
       
 