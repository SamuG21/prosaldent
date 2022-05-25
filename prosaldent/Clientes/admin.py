from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Cliente, ClienteAdmin)
