from django.contrib import admin
from .models import Floor

# Register your models here.
class FloorAdmin(admin.ModelAdmin):
    list_display = ('floor','wait_time', 'passenger')
    
admin.site.register(Floor, FloorAdmin)