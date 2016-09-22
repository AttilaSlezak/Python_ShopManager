import unittest
from datetime import datetime
from Shop.milk import Milk
from Shop.shop import Shop
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.test_shop = Shop("Food Store", "101st Corner Street", "George Warren")
        self.test_milk = Milk(101, Milk.LITER, "Plain Milk inc.", datetime.today(), Milk.WHOLE_MILK)

    def tearDown(self):
        self.test_shop = None
        self.test_milk = None

    def test_name(self):
        self.assertEqual("Food Store", self.test_shop.name())

    def test_address(self):
        self.assertEqual("101st Corner Street", self.test_shop.address())

    def test_owner(self):
        self.assertEqual("George Warren", self.test_shop.owner())

    def test_is_there_any_milk_if_not(self):
        self.assertFalse(self.test_shop.is_there_any_milk())

    def test_is_there_any_milk_if_yes(self):
        self.test_shop.replenish_milk_counter(self.test_milk)
        self.assertTrue(self.test_shop.is_there_any_milk())

    def test_replenish_milk_counter(self):
        self.test_shop.replenish_milk_counter(self.test_milk)
        self.assertTrue(self.test_shop.is_there_any_milk())

    def test_buy_milk(self):
        self.test_shop.replenish_milk_counter(self.test_milk)
        self.assertEqual(self.test_milk, self.test_shop.buy_milk(101))

if __name__ == '__main__':
    unittest.main()
