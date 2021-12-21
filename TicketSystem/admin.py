from django.contrib import admin
from TicketSystem.models import UserInfo
from TicketSystem.models import Airlines
from TicketSystem.models import FlightInfo

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Airlines)
admin.site.register(FlightInfo)