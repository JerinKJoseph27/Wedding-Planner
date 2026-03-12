from django.contrib import admin
from .models import Enqry


@admin.register(Enqry)
class EnqryAdmin(admin.ModelAdmin):
	list_display = ("id", "p_name", "p_email", "p_phone", "p_when", "p_events")
	search_fields = ("p_name", "p_email", "p_phone", "p_events")
	list_filter = ("p_events", "p_when")
	ordering = ("-id",)