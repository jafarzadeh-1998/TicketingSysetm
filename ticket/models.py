from django.db import models
from django.urls import reverse

# Create your models here.


class Ticket(models.Model):
        title = models.CharField(max_length = 200)
        user = models.CharField(max_length=200)
        def __str__ (self):
                return self.title

        def get_absolute_url(self):
                return reverse('ticket:ticket-detail', args=[str(self.id)])



class TicketMessage(models.Model):
        message = models.CharField(max_length=200)
        ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE) 
        def __str__ (self):
                return self.message



