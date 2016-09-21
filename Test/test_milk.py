import unittest
from datetime import datetime, timedelta
from Shop import milk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class MyTestCase(unittest.TestCase):

    def test_incorrect_data_to_initialize_milk(self):
        with self.assertRaises(ValueError):
            milk.Milk(1000, "Plain Milk inc.", datetime.strptime("2017-01-01", "%Y-%m-%d"), 28, 210)

    def test_is_milk_still_under_guarantee(self):
        test_date = datetime.today() + timedelta(days=1)
        test_milk = milk.Milk(1000, "Plain Milk inc.", test_date, 2.8, 210)
        self.assertEqual(True, test_milk.check_still_under_guarantee())

    def test_str_method(self):
        test_milk = milk.Milk(1000, "Plain Milk inc.", datetime.strptime("2017-01-01", "%Y-%m-%d"), 2.8, 210)
        self.assertEqual("Milk{cubicCapacity: 1000 ml, producer: 'Plain Milk inc.', bestBefore: 2017-01-01 00:00:00" +
                         ", fatContent: 2.8, price: 210 forint(s)}", test_milk.__str__())

if __name__ == '__main__':
    unittest.main()
