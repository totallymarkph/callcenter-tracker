from django.contrib import admin
from .models import CallCenterAgent, Team, Call

admin.site.register(CallCenterAgent)
admin.site.register(Team)
admin.site.register(Call)