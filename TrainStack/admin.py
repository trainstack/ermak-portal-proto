from django.contrib import admin
from TrainStack.models import topology

class topologyAdmin(admin.ModelAdmin):
    pass
admin.site.register(topology, topologyAdmin)