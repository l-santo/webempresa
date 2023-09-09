from django.contrib import admin
from .models import Service
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','update') # Configuracion extendida sobre el admin
    

admin.site.register(Service, ServiceAdmin)