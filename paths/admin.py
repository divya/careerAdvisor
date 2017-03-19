from django.contrib import admin

# Register your models here.
from .models import Users, Linkentries, Milentries, Nodetypes, Nodes, Patentries, Pubentries, Skillentries, Skillnames, Trajectoryentries, Trajectorytemp


admin.site.register(Users)
admin.site.register(Linkentries)
admin.site.register(Milentries)
admin.site.register(Nodetypes)
admin.site.register(Nodes)
admin.site.register(Patentries)
admin.site.register(Pubentries)
admin.site.register(Skillentries)
admin.site.register(Skillnames)
admin.site.register(Trajectoryentries)
admin.site.register(Trajectorytemp)
