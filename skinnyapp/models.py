from django.db import models

# Create your models here.

class slug(models.Model):
	id = models.AutoField(primary_key = True)
	url = models.URLField
	slug = models.SlugField(max_length = 50)

	class Meta:
		db_table = 'slugs'

class lookup(models.Model):
	slug_id = models.OneToOneField(slug, on_delete = models.CASCADE, primary_key = True)
	ip_address = models.GenericIPAddressField  
	referrer = models.URLField
	when = models.DateField(auto_now_add = True)

	class Meta:
		db_table = 'lookups'
