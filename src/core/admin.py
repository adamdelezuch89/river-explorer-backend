from django.contrib import admin
from .models import RiverSegment

# Register your models here.

@admin.register(RiverSegment)
class RiverSegmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'flow_direction', 'flow_rate']
    list_filter = ['name']
    search_fields = ['id', 'name']
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False