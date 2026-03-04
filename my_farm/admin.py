

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(FarmHand)

admin.site.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'location']

admin.site.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['crop_name', 'id', 'farm', 'harvest_date', 'qr_generated']
    readonly_fields = ['id']

admin.site.register(TreatmentLog)
class TreatmentLogAdmin(admin.ModelAdmin):
    list_display = ['batch', 'action_type', 'date', 'product_used']
    
    
admin.site.register(new_farmhand)