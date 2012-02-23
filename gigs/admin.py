from django.contrib import admin

from models import venue, gig, performance, tour

class gigsAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ('name',)

admin.site.register(gig, gigsAdmin)
admin.site.register(performance, gigsAdmin)
admin.site.register(venue, gigsAdmin)
admin.site.register(tour, gigsAdmin)
