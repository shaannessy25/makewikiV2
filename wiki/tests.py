import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from wiki.models import Page
# Create your tests here.

class WikiTestCase(TestCase):
    def test_true_is_true(self):
        '''test that True equals True'''
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        '''test the slug generated when saving a page'''
        
        # create a user to test 
        user = User()
        user.save()

        # create a and save page to DB
        page = Page(title='My test page', content='test', author=user)
        page.save()

        self.assertEqual(page.slug, 'my-test-page')

class PageListViewTests(TestCase):
    '''Tests that the homepage works'''
    def test_multiple_pages(self):
        # create a user to test 
        user = User.objects.create()

        # create a and save page to DB
        Page(title='My test page', content='test', author=user)
        Page(title='Another test page', content='test again', author=user)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

class PageDetailsView(TestCase):
    '''Tests that the page is created properly'''
    def test_page_load(self):
        '''tests to make sure the page is loading properly'''
        # create a user to test 
        user = User.objects.create()

        # create a and save page to DB
        page = Page(title='My test page', content='test', author=user)
        page.save()

        response = self.client.get(f'/{page.slug}')

        self.assertEqual(response.status_code, 301)

    def test_page_contents(self):
        '''tests if the page is displaying correctly'''
        # create a user to test 
        user = User.objects.create()

        # create a and save page to DB
        page = Page(title='My test page', content='test', author=user)
        page.save()

        response = self.client.get(f'/{page.slug}')

        self.assertEqual(response.page.title, 'my test page')
