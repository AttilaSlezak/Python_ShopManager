from Shop.long_life_milk import LongLifeMilk
from Shop.semi_long_life_milk import SemiLongLifeMilk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class MilkFactory(object):

    @staticmethod
    def new_long_life_milk(barcode, cubic_capacity, producer, best_before, fat_content):
        return LongLifeMilk(barcode, cubic_capacity, producer, best_before, fat_content)

    @staticmethod
    def new_semi_long_life_milk(barcode, cubic_capacity, producer, best_before, fat_content):
        return SemiLongLifeMilk(barcode, cubic_capacity, producer, best_before, fat_content)
