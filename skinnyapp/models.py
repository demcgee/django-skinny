from django.db import models

# Create your models here.

class slug(models.Model):
    id = models.AutoField(primary_key = True)
    url = models.URLField(null = False, blank = False, default = "http://skinny.dev")
    slug = models.SlugField(null = False, blank = False, max_length = 50)

    class Meta:
        db_table = 'slugs'

class lookup(models.Model):
    id = models.AutoField(primary_key = True)
    slug_id = models.ForeignKey(slug, on_delete = models.CASCADE)
    ip_address = models.GenericIPAddressField(null = True)
    referrer = models.URLField(null = True)
    when = models.DateField(auto_now_add = True)

    class Meta:
        db_table = 'lookups'
