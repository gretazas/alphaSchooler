from django.contrib import admin
from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rate_id', 'rate_amount', 'date')


admin.site.register(Rating, RatingAdmin)
