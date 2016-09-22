import unittest
import inspect
from datetime import datetime
from Shop.shop import Shop
from Shop.milk import Milk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class MyTestCase(unittest.TestCase):

    def setUp(self):
        test_shop = Shop("Food Store", "101st Corner Street", "George Warren")
        self.test_milk = Milk(101, Milk.LITER, "Plain Milk inc.", datetime.today(), Milk.WHOLE_MILK)

        class_shop_reg = getattr(test_shop, '_Shop__ShopRegister')
        self.shop_reg = class_shop_reg(self.test_milk, 3, 100)
        self.methods_shop_reg = inspect.getmembers(self.shop_reg, predicate=inspect.ismethod)

    def tearDown(self):
        self.test_milk = None
        self.shop_reg = None
        self.methods_shop_reg = None

    def execute_private_method(self, method_name, new_obj=None):
        method = getattr(self.shop_reg, method_name)
        if new_obj is None:
            method()
        else:
            method(new_obj)

    def test_get_milk(self):
        self.assertEqual(self.test_milk, self.shop_reg.milk())

    def test_set_milk(self):
        new_milk = Milk(201, Milk.HALF_LITER, "Other Milk inc.", datetime.today(), Milk.LOW_FAT_MILK)
        self.shop_reg.milk(new_milk)
        self.assertEqual(new_milk, self.shop_reg.milk())

    def test_get_quantity(self):
        self.assertEqual(3, self.shop_reg.quantity())

    def test_set_quantity(self):
        self.shop_reg.quantity(10)
        self.assertEqual(10, self.shop_reg.quantity())

    def test_get_price(self):
        self.assertEqual(100, self.shop_reg.price())

    def test_set_price(self):
        self.shop_reg.price(200)
        self.assertEqual(200, self.shop_reg.price())

    def test_add_quantity(self):
        start_quantity = self.shop_reg.quantity()
        difference = 5
        self.execute_private_method("add_quantity", difference)
        self.assertEqual(start_quantity + difference, self.shop_reg.quantity())

    def test_subtract_quantity(self):
        start_quantity = self.shop_reg.quantity()
        difference = 2
        self.execute_private_method("subtract_quantity", difference)
        self.assertEqual(start_quantity - difference, self.shop_reg.quantity())

if __name__ == '__main__':
    unittest.main()
