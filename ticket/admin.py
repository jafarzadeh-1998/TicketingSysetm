from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TicketMessage)
class TicketMessage(admin.ModelAdmin):
    pass