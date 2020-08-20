from django.test import TestCase, Client
from django.urls import reverse
from store.models import Category, Customer, Product
import json
from django_webtest import WebTest



#  Using WebTest


class TestViews(WebTest):

    def test_home(self):
        url = reverse("home")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


    def test_signup_GET(self):
        url = reverse("signup")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)    



    def test_signup_POST(self):

        url = reverse('signup')

        resp = self.client.post(url, {
        'name' : 'name',
        'email' : 'email',
        'phone' : 'phone',
        'password1' : 'password1',
        'password2' : 'password2'
        })

        self.assertEqual(resp.status_code, 200)    

    def test_login_GET(self):

        url = reverse('login')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)  


    def test_login_POST(self):

        url = reverse('login')

        resp = self.client.post(url, {
            'email' : 'email',
            'password1' : 'password1'
            })  

        self.assertEqual(resp.status_code, 200)      



    def test_nearest_restaurants_GET(self):

        url = reverse('nearest_restaurants')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)      

  



# Using Test Case


# class TestViews(TestCase):
#     # Setup code
#     def setUp(self):
#         self.client = Client()
#         self.home_url = reverse('home')
#         self.signup_url = reverse('signup')
#         self.login_url = reverse('login')
#         self.nearest_restaurants_url = reverse('nearest_restaurants')

#     # Test code
#     def test_index_GET(self):
#         response = self.client.get(self.home_url)

#         # Assertions
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html')


#     def test_signup_GET(self):
#         response = self.client.get(self.signup_url)

#         # Assertions
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'signup.html')

#     def test_signup_POST(self):
#         response = self.client.post(self.signup_url, {
#             'name' : 'name',
#             'email' : 'email',
#             'phone' : 'phone',
#             'password1' : 'password1',
#             'password2' : 'password2'
#         })

#         self.assertEquals(response.status_code, 200)


#     def test_signup_POST(self):
#         response = self.client.post(self.signup_url, {
#             'name' : 'name',
#             'email' : 'email',
#             'phone' : 'phone',
#             'password1' : 'password1',
#             'password2' : 'password2'
#         })

#         self.assertEquals(response.status_code, 200)  


#     def test_login_GET(self):
#         response = self.client.get(self.login_url)

#         # Assertions
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'login.html')  


#     def test_login_POST(self):
#         response = self.client.post(self.login_url, {
#             'email' : 'testgmail.com',
#             'password1' : 'password1',
#         })

#         self.assertEquals(response.status_code, 200)   


#     def test_nearest_restaurants_GET(self):
#         response = self.client.get(self.nearest_restaurants_url)

#         # Assertions
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nearest_restaurants.html')




    
        


        


