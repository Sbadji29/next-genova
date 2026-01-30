from django.contrib import admin
from .models import *


class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'site_web', 'ordre')
    ordering = ('ordre', 'nom')

class PaysAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'ordre')
    ordering = ('ordre', 'nom')

class VisaAdmin(admin.ModelAdmin):
    list_display = ('titre', 'pays', 'ordre')
    list_filter = ('pays',)
    ordering = ('ordre', 'titre')

admin.site.register(Apropos)
admin.site.register(Service)
admin.site.register(Realisation)
admin.site.register(Contact)
admin.site.register(Partenaire, PartenaireAdmin)
admin.site.register(Pays, PaysAdmin)
admin.site.register(Visa, VisaAdmin)

