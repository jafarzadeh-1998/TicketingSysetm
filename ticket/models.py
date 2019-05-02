from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.


class Ticket(models.Model):
        title = models.CharField(max_length=300)
        user = models.ForeignKey(User ,on_delete=models.CASCADE)
        def __str__ (self):
                return self.title

        def get_absolute_url(self):
                return reverse('ticket:ticket-detail', args=[str(self.id)])



class TicketMessage(models.Model):
        message  = models.CharField(max_length=300)
        ticket   = models.ForeignKey(Ticket,on_delete=models.CASCADE) 
        reply    = models.CharField(max_length=300 ,default="")
        
        def __str__ (self):
                return self.ticket.title + " : " + self.message



