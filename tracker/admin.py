from django.contrib import admin
from tracker.models import Task, Resource, TimeSpent, Cost
# Register your models here.
admin.site.register(Task)
admin.site.register(Resource)
admin.site.register(TimeSpent)
admin.site.register(Cost)
