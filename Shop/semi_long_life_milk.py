from Shop.milk import Milk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class SemiLongLifeMilk(Milk):

    def __init__(self, barcode, cubic_capacity, producer, best_before, fat_content):
        Milk.__init__(barcode, cubic_capacity, producer, best_before, fat_content)
