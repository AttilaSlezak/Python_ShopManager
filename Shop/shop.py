from Shop.milk import Milk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Shop(object):

    def __init__(self, name, address, owner, milk_counter=None):
        if milk_counter is None:
            milk_counter = {}

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
        if type(milk) != Milk:
            return False

        shop_reg = self.milk_counter.get(milk.barcode)
        if shop_reg is None:
            shop_reg = Shop.__ShopRegister(milk, 1, 100)
            self.milk_counter[milk.barcode] = shop_reg
        else:
            shop_reg.add_quantity(1)

    def buy_milk(self, barcode):
        shop_reg = self.milk_counter[barcode]
        if shop_reg is not None:
            shop_reg.subtract_quantity(1)
            return shop_reg.milk
        return None

    class __ShopRegister(object):

        def __init__(self, milk, quantity, price):
            self.milk = milk
            self.quantity = quantity
            self.price = price

        def add_quantity(self, quantity):
            self.quantity += quantity

        def subtract_quantity(self, quantity):
            self.quantity -= quantity
