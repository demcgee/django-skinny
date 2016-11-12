from django.shortcuts import render, get_object_or_404
from skinnyapp.models import slug
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf 
import random, string, json

# Create view for home page
def home(request):
  return render(request, 'skinnyapp/home.html', {})

# Create view for original URL when short URL is requested
def redirect(request, slug):
    url = get_object_or_404(slug, pk=slug)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.url)

# Create view for short URL creation
def shorten(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        slug = slug()
        b = slug(url=url, slug=slug)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + slug
        return HttpResponse(json.dumps(response_data), content_type="application/json")

# Create view for slug
def slug():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = slug.objects.get(pk=slug)
        except:
            return slug