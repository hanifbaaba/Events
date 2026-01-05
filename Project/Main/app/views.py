from django.shortcuts import render

from rest_framework import viewsets, status
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Events
from .serializers import EventsSerializer
# from django.utils.timezone import now
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Events
from .serializers import EventsSerializer
# from rest_framework import filters
# from rest_framework import status as drf_status
# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from .permissions import IsEventCreatorOrReadOnly
# from django.db.models import Q

class EventsView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,IsEventCreatorOrReadOnly]
    # permission_classes = [AllowAny]
    # parser_classes = [MultiPartParser, FormParser,JSONParser]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['category_of_event',]
    # search_fields = ['name_of_event', 'venue_of_event']
    # ordering_fields = ['date_of_event']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_serializer_context(self):
        return {'request': self.request}

    # def get_queryset(self):
        # return Events.objects.all()
        # return Events.objects.filter( Q(date_of_event__gte=now()) | Q(date_of_event__isnull=True))
            
            # date_of_event__gte=now()).order_by('-created_at')
    
   
        
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=400)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=201)
    
    # @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    # def rsvp(self, request, pk=None):
    #     event = self.get_object()
    #     status_value = request.data.get('status')

    #     if status_value not in ['going', 'interested']:
    #         return Response(
    #             {"error": "status must be 'going' or 'interested'"},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     try:
    #         rsvp, created = RSVP.objects.get_or_create(
    #             event=event,
    #             user=request.user,
    #             defaults={'status': status_value}
    #         )
    #         if not created:
    #             rsvp.status = status_value
    #             rsvp.save()
    #     except Exception as e:
    #         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    #     return Response(RSVPSerializer(rsvp).data, status=status.HTTP_200_OK)