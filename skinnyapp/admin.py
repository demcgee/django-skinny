from django.contrib import admin
from skinnyapp.models import Slug, Lookup
# Register your models here.

class slug_admin(admin.ModelAdmin):
	list_display = ('id', 'url','slug')

class lookup_admin(admin.ModelAdmin):
	list_display = ('id', 'slug_id', 'ip_address', 'referrer', 'when')

admin.site.register(Slug, slug_admin)
admin.site.register(Lookup, lookup_admin)