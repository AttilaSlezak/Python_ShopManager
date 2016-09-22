import unittest
from datetime import datetime, timedelta
from Shop.milk import Milk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class MyTestCase(unittest.TestCase):

    test_date = datetime.today() + timedelta(days=1)

    def setUp(self):
        self.test_milk = Milk(101, Milk.LITER, "Plain Milk inc.", MyTestCase.test_date, Milk.WHOLE_MILK)

    def tearDown(self):
        self.test_milk = None

    def test_barcode(self):
        self.assertEqual(101, self.test_milk.barcode())

    def test_cubic_capacity(self):
        self.assertEqual(1000, self.test_milk.cubic_capacity())

    def test_producer(self):
        self.assertEqual("Plain Milk inc.", self.test_milk.producer())

    def test_best_before(self):
        self.assertEqual(MyTestCase.test_date, self.test_milk.best_before())

    def test_fat_content(self):
        self.assertEqual(2.8, self.test_milk.fat_content())

    def test_incorrect_data_to_initialize_milk(self):
        with self.assertRaises(ValueError):
            Milk(101, Milk.LITER, "Plain Milk inc.", MyTestCase.test_date, 28)

    def test_is_milk_still_under_guarantee(self):
        self.assertEqual(True, self.test_milk.check_still_under_guarantee())

    def test_str_method(self):
        self.assertEqual("Milk{barcode: 101, cubic capacity: 1000 ml, producer: 'Plain Milk inc.', best before: " +
                         str(MyTestCase.test_date) + ", fat content: 2.8}", self.test_milk.__str__())

if __name__ == '__main__':
    unittest.main()
