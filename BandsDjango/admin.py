from django.contrib import admin
from .models import Event, Band





admin.site.register(Event, EventAdmin)
admin.site.register(Band, BandAdmin) bla


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'created_by')
    readonly_fields = ('created_by',)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

