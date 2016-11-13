from django.test import TestCase
from django.core.exceptions import ValidationError

from skinnyapp.models import Slug

class SlugTestCase(TestCase):
    def setUp(self):
        Slug.objects.create(slug="goog", url="http://google.com")

    def test_slugs_must_have_slug(self):
        """slugs need to have slugs to exist"""
        try:
            subject = Slug(url="http://example.com")
            subject.full_clean()
            self.fail("slugs need slugs")
        except ValidationError as e:
            pass

    def test_slugs_must_have_urls(self):
        """slugs need to have urls to exist"""
        try:
            subject = Slug(slug = "missing-url")
            subject.full_clean()
            self.fail("slugs without urls shouldn't validate")
        except ValidationError as e:
            # check for good error messages
            pass

    def test_slugs_without_urls_do_not_save(self):
        """slugs should not save to the db without a url"""
        current_count = Slug.objects.count()
        Slug.objects.create(slug="broken-url")
        self.assertEqual(Slug.objects.count(), current_count)

    def test_slugs_without_slug_do_not_save(self):
        """slugs should not save to the db without a slug"""
        current_count = Slug.objects.count()
        Slug.objects.create(url="http://example.com")
        self.assertEqual(Slug.objects.count(), current_count)

    def test_urls_must_be_valid(self):
        """urls should actually be urls"""
        try:
            subject = Slug(slug="invalid-url", url="this-is-not-a-url")
            subject.full_clean()
            self.fail("invalid urls shouldn't pass validation")
        except ValidationError as e:
            # check for good error message
            pass
    def test_urls_must_be_real(self):
        """urls should exist when they are created"""
        try:
            subject = Slug(slug="invalid-url", url="http://its-unlikely-this-will-work.info")
            subject.full_clean()
            self.fail("urls that don't exist shouldn't pass validation")
        except ValidationError as e:
            # check for good error message
            pass

