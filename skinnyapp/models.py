from django.db import models

# Create your models here.

class Slug(models.Model):

    id = models.AutoField(primary_key = True)
    url = models.URLField(null = False, blank = False, default = "http://skinny.dev")
    slug = models.SlugField(null = False, blank = False, max_length = 50)

    class Meta:
        db_table = 'slugs'

    def __str__(self):
        return self.url


    @classmethod
    def create(cls, url):
        slug = cls()
        #slug.slug = # create a unique string
        slug.url = url
        return slug

class Lookup(models.Model):
    id = models.AutoField(primary_key = True)
    slug_id = models.ForeignKey(Slug, on_delete = models.CASCADE)
    ip_address = models.GenericIPAddressField(null = True)
    referrer = models.URLField(null = True)
    when = models.DateField(auto_now_add = True)

    class Meta:
        db_table = 'lookups'
        
    def __str__(self):
        return self.slug_id
