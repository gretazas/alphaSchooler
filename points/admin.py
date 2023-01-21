from django.contrib import admin
from django.contrib import admin
from .models import Points


class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'date')


admin.site.register(Points, PointsAdmin)
