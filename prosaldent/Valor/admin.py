from django.contrib import admin
from .models import Valor, Opi

class ValorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class OpiAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Valor, ValorAdmin)
admin.site.register(Opi, OpiAdmin)