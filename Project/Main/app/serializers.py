
from rest_framework import serializers
from .models import Events
from django.utils.timezone import now

class EventsSerializer(serializers.ModelSerializer):
    # rsvp_count = serializers.SerializerMethodField()
    # my_rsvp_status = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.id')
    photo_of_event = serializers.ImageField(required=False, allow_null=True)


    class Meta:
        model = Events
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at',]
       
    # def get_rsvp_count(self, obj):
        # return obj.rsvps.count()

    # def get_my_rsvp_status(self, obj):
    #     request = self.context.get('request')
    #     if request and request.user.is_authenticated:
    #         rsvp = obj.rsvps.filter(user=request.user).first()
    #         return rsvp.status if rsvp else None
    #     return None

# class RSVPSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RSVP
#         fields = ['id', 'event', 'status', 'created_at']
#         read_only_fields = ['event','created_at']
