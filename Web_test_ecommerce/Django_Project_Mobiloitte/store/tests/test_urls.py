from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import index, signup, login, nearest_restaurants


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)


    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup)


    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)   


    def test_nearest_restaurants_url_is_resolved(self):
        url = reverse('nearest_restaurants')
        print(resolve(url))
        self.assertEquals(resolve(url).func, nearest_restaurants)     


        

