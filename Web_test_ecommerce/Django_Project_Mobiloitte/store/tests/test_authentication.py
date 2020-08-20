# from django.test import TestCase
# from django.urls import reverse

# class BaseTest(TestCase):
#     def setUp(self):
#         self.signup_url = reverse('signup')
#         self.user = {
#             'name' : 'name',
#             'email' : 'email',
#             'phone' : 'phone',
#             'password1' : 'password1',
#             'password2' : 'password2'

#         }

#         self.user_short_password = {
#             'name' : 'name',
#             'email' : 'email',
#             'phone' : 'phone',
#             'password1' : 'tes',
#             'password2' : 'tes'

#         }


#         return super().setUp()


# class SignupTest(BaseTest):
#     def test_can_view_page_correctly(self):
#         response = self.client.get(self.signup_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'signup.html')


#     def test_can_signup_user(self):
#         response = self.client.post(self.signup_url,self.user, format= 'text/html')    
#         self.assertEqual(response.status_code, 200)



#     def test_cant_signup_user_withshortpassword(self):
#         response = self.client.post(self.signup_url,self.user_short_password, format= 'text/html')    





