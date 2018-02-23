from django.contrib import admin
from .models import Domain, Registrar
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment

# Register your models here.


class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'updatetime', 'description', 'type', 'registry', 'status', 'cate', 'popular', 'restrictions', 'sources',)

admin.site.register(Domain, DomainAdmin)
admin.site.register(Registrar)



# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'tags')

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
