from django_webtest import WebTest
from store.models import Customer, Category, Product
from django.utils import timezone
from django.urls import reverse
 


class TestModels(WebTest):
    
    def create_customer(self, name= 'steve', email='steve@gmail.com'):
        return Customer.objects.create(name=name, email=email)

    def test_customer_creation(self):
        w = self.create_customer()
        self.assertTrue(isinstance, (w, Customer))


    def create_product(self):
        category = Category.objects.create(name='Cloth-Men')
        return Product.objects.create(category= category)

    def test_product_creation(self):
        w = self.create_product()
        self.assertTrue(isinstance, (w, Product))    


    def create_category(self, name= 'Men-Shoes'):
        return Category.objects.create(name=name)


    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance, (w, Category))    










 

