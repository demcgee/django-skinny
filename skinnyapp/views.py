from django.shortcuts import render

# Create your views here.

# Create view for home page
def home(request):
  return render(request, 'skinnyapp/home.html', {})

# Create view for original URL when short URL is requested

# Create view for short URL creation

# Create view for slug