from django.test import TestCase
from Restaurant.models import Menu


class MenuTest(TestCase):

    def test_menu_name(self):
        item = Menu.objects.create(
            title="IceCream",
            price=80,
            description="Vanilla ice cream",
            inventory=100
        )

        self.assertEqual(str(item), "IceCream")