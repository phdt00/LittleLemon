from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=75.99, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 75.99")