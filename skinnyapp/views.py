from django.shortcuts import render, get_object_or_404
from skinnyapp.models import Slug
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings
from django.template.context_processors import csrf 
from django.views.decorators.csrf import csrf_exempt
import random, string, json

# Create view for home page
def home(request):
  return render(request, 'skinnyapp/home.html', {})

# Create view for original URL when short URL is requested
@csrf_exempt
def redirect(request, slug):
    url = get_object_or_404(Slug, slug=slug)
    url.save()
    return HttpResponseRedirect(url.url)

# Create view for short URL creation
@csrf_exempt
def shorten(request):
    myurl = request.POST.get("url", '')
    if not (myurl == ''):
        the_slug = Slug.objects.filter(url=myurl).first()
        if (the_slug == None):
            the_slug = Slug(url=myurl, slug=generate_slug())
            the_slug.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + the_slug.slug
        return JsonResponse(response_data)

# helper function!
def generate_slug():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        slug = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Slug.objects.get(slug=slug)
        except:
            return slug