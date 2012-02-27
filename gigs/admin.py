from django.contrib import admin

from models import venue, gig, performance, tour

class gigsAdmin(admin.ModelAdmin):
	ordering = ('id',)
	search_fields = ('name',)

class performanceInline(admin.TabularInline):
	model = performance
	extra = 1

class gigAdmin(admin.ModelAdmin):
	inlines = [performanceInline,]
	ordering = ('date',)
	search_fields = ('name',)

admin.site.register(gig, gigAdmin)
admin.site.register(venue, gigsAdmin)
admin.site.register(tour, gigsAdmin)
