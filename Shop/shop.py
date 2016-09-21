# -- coding: utf-8 --
__author__ = 'Slezak Attila'
from Shop.milk import Milk


class Shop(object):

    def __init__(self, name, address, owner, milk_counter={}):
        if not Shop.check_data_can_represent_real_shop(name, address, owner, milk_counter):
            raise ValueError("Given data cannot represent a real Shop!")

        self.name = name
        self.address = address
        self.owner = owner
        self.milk_counter = milk_counter

    @staticmethod
    def check_data_can_represent_real_shop(name, address, owner, milk_counter):
        if type(name) != str:
            print("'name' must be string type!")
            return False
        elif type(address) != str:
            print("'address' must be string type!")
            return False
        elif type(owner) != str:
            print("'owner' must be string type!")
            return False
        elif type(milk_counter) != dict:
            print("'milk_counter' must be dictionary type!")
            return False
        return True

    def is_there_any_milk(self):
        return len(self.milk_counter) > 0

    def replenish_milk_counter(self, milk):
        if type(milk) != Milk: return False
        self.milk_counter[milk.barcode] = milk

    def buy_milk(self, barcode):
        return self.milk_counter.pop(barcode, None)
