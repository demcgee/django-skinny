from django.contrib import admin
from skinnyapp.models import slug, lookup
# Register your models here.

class slug_admin(admin.ModelAdmin):
	list_display = ('id', 'url','slug')

class lookup_admin(admin.ModelAdmin):
	list_display = ('slug_id', 'ip_address', 'referrer', 'when')

admin.site.register(slug, slug_admin)
admin.site.register(lookup, lookup_admin)