from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'details', 'date',)
    list_filter = ('customer_name', 'date',)
    search_fields = ('customer_name', 'details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)

