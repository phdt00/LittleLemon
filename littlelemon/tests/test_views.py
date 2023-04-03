from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(
            title="Rice",
            price=10,
            inventory=50
        )
        Menu.objects.create(
            title="Bulgur",
            price=25,
            inventory=100
        )
    
    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        request = self.factory.get('restaurant/menu/items/')
        response = MenuItemsView.as_view()(request)
        self.assertEqual(response.data, serialized_items.data)

