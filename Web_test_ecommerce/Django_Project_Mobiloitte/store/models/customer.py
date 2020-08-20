from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)



    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)   

        except:
            return False      


    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False       





