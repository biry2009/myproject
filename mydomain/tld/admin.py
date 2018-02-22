from django.contrib import admin
from .models import Domain, Registrar

# Register your models here.


class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'updatetime', 'description', 'type', 'registry', 'status', 'cate', 'popular', 'restrictions', 'sources',)

admin.site.register(Domain, DomainAdmin)
admin.site.register(Registrar)
