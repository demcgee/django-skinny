from django.test import TestCase, Client
from skinnyapp.models import slug, lookup
import json

client = Client()

class ResponsesTestCase(TestCase):
    def setUp(self):
        subject =  slug.objects.create(slug="goog", url="http://google.com")
        lookup.objects.create(slug_id=subject, referrer="http://skinny.test",
                ip_address="127.0.0.1")

    def test_post_url_creates_slug(self):
        """posting a new url creates a slug"""
        response = client.post("/", {'url': "http://github.com"})
        self.assertEqual(response.status_code, 201)
        try:
          body = json.loads(response.content)
          self.assertIn('location', body.keys())
          self.assertIsNot(body['location'], None)
        except Exception as e:
          self.fail("json parsing probably went south")

    def test_post_existing_url_returns_location(self):
        """posting a new url creates a slug"""
        response = client.post("/", {'url': "http://google.com"})
        self.assertEqual(response.status_code, 200)
        try:
          body = json.loads(response.content)
          self.assertIn('location', body.keys())
          self.assertRegex(body['location'], re.compile('/goog$'))
        except Exception as e:
          self.fail("json parsing probably went south")

    def test_posting_crap_fails(self):
        """posting an existing url returns a location"""
        response = client.post("/", {'url': "garbage"})
        self.assertEqual(response.status_code, 400)

    def test_getting_existing_slug_forwards(self):
        """getting an existing slug returns a forward"""
        response = client.get("/goog")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], "http://google.com")

    def test_getting_unknown_slug_errors(self):
        """getting an unknown slug returns a 404"""
        response = client.get("/wat")
        self.assertEqual(response.status_code, 404)

    def test_stats_return_lookup_count(self):
        """statting a slug returns its lookup count"""
        google_slug = slug.objects.get(slug="goog")
        lookup_count = lookup.objects.filter(slug_id = google_slug).count()

        response = client.get("/stats/goog")
        self.assertEqual(response.status_code, 200)
        try:
          body = json.loads(response.content)
          self.assertIn('lookups', body.keys())
          self.assertEqual(body['lookups'], lookup_count)
        except Exception as e:
          self.fail("json parsing probably went south")

    def test_getting_unknown_slug_errors(self):
        """statting an unknown slug returns a 404"""
        response = client.get("/stats/wat")
        self.assertEqual(response.status_code, 404)


