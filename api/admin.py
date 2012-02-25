from django.contrib import admin

from models import rid

class apiAdmin(admin.ModelAdmin):
    ordering = ('id',)

admin.site.register(rid, apiAdmin)
