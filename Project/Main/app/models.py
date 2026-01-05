from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    name_of_event = models.CharField(max_length=200)
    date_of_event = models.DateTimeField(blank=True,null=True)
    venue_of_event = models.TextField()
    photo_of_event = models.ImageField(upload_to="event_image/",blank=True,null=True)
    description_of_event = models.TextField(null=True, blank=True)
    number_of_tickets = models.PositiveIntegerField()
    price_of_tickets = models.DecimalField(decimal_places=2, max_digits=10, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    CATEGORY_CHOICES = (
        ('parties', 'Parties'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('conference', 'Conference'),
    )
    
    category_of_event = models.CharField(max_length=100, choices = CATEGORY_CHOICES, blank=True,null=True)
    
    def __str__(self):
        return self.name_of_event
   
# class RSVP(models.Model):
#     STATUS_CHOICES = (
#         ("going", "Going"),
#         ("interested", "Interested"),
#     )
#     event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="rsvps")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rsvps")
#     status = models.CharField(max_length=20, choices= STATUS_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         unique_together = ('event', 'user')
#         indexes = [
#         models.Index(fields=['event', 'user']),
#     ]

#     def __str__(self):
#         return f"{self.user.username} → {self.event.name_of_event} ({self.status})"