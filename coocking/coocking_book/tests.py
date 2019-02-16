from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate
# Create your tests here.
from django.urls import reverse
from .models import *
# Create your tests here.


class CoockingBookTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ingredient_1 = Ingredient.objects.create(
            name='Ингредиент№1', weight=500)
        cls.ingredient_2 = Ingredient.objects.create(
            name='Ингредиент№2', weight=500)
        cls.dish_1 = Dish.objects.create(
            title='dish1', description='description1')
        cls.dish_1.ingredient.set([cls.ingredient_1, cls.ingredient_2])
        cls.dish_1.save()
        user = User.objects.create_user(
            'username1', 'myemail@username1.com', 'myuserpassword')
        permissions = Permission.objects.all()
        for p in permissions:
            user.user_permissions.add(p)
        user.save()

    def test_order_add(self):
        count = Order.objects.count()
        content_data = {'contact': '456468',
                        'form-TOTAL_FORMS': '3',
                        'form-INITIAL_FORMS': '2',
                        'form-MIN_NUM_FORMS': '0',
                        'form-MAX_NUM_FORMS': '1000',
                        'form-0-name': self.ingredient_1.name,
                        'form-0-weight': self.ingredient_1.weight,
                        'form-0-id': self.ingredient_1.id,
                        'form-1-name': self.ingredient_2.name,
                        'form-1-weight': self.ingredient_1.weight,
                        'form-1-id': self.ingredient_2.id,
                        }
        order_list_url = reverse('coocking_book:add_order_list', kwargs={
                                 'dish_id': self.dish_1.id})
        self.client.login(username='username1', password='myuserpassword')
        self.client.post(order_list_url, data=content_data)
        self.assertEquals(Order.objects.count(), count + 1)

    def test_order_add_fail(self):
        count = Order.objects.count()
        content_data = {'contact': '456468',
                        'form-TOTAL_FORMS': '3',
                        'form-INITIAL_FORMS': '2',
                        'form-MIN_NUM_FORMS': '0',
                        'form-MAX_NUM_FORMS': '1000',
                        'form-0-name': '',
                        'form-0-weight': '',
                        'form-0-id': self.ingredient_1.id,
                        'form-1-name': '',
                        'form-1-weight': '',
                        'form-1-id': self.ingredient_2.id,
                        }
        order_list_url = reverse('coocking_book:add_order_list', kwargs={
                                 'dish_id': self.dish_1.id})
        self.client.login(username='username1', password='myuserpassword')
        self.client.post(order_list_url, data=content_data)
        self.assertNotEquals(Order.objects.count(), count + 1)

    def test_add_ingredient(self):
        count = Ingredient.objects.filter(dishes=self.dish_1.id).count()
        ingredient = Ingredient.objects.create(
            name='Ингредиент№3', weight=100)
        content_data = {'form-TOTAL_FORMS': '10',
                        'form-INITIAL_FORMS': '0',
                        'form-MIN_NUM_FORMS': '0',
                        'form-MAX_NUM_FORMS': '1000',
                        'form-0-name': ingredient.name,
                        'form-0-weight': ingredient.weight,
                        'form-0-id': ingredient.id,
                        }
        add_ingredient_url = reverse('coocking_book:add_ingredients', kwargs={
                                     'dish_id': self.dish_1.id})
        self.client.login(username='username1', password='myuserpassword')
        self.client.post(add_ingredient_url, data=content_data)
        self.assertEquals(Ingredient.objects.filter(
            dishes=self.dish_1.id).count(), count + 1)
