from Shop.milk import Milk
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Shop(object):

    def __init__(self, name, address, owner, milk_counter=None):
        if milk_counter is None:
            milk_counter = {}

        if not Shop.check_data_can_represent_real_shop(name, address, owner, milk_counter):
            raise ValueError("Given data cannot represent a real Shop!")

        self.__name = name
        self.__address = address
        self.__owner = owner
        self.__milk_counter = milk_counter

    def name(self):
        return self.__name

    def address(self):
        return self.__address

    def owner(self):
        return self.__owner

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
        return len(self.__milk_counter) > 0

    def replenish_milk_counter(self, milk):
        if type(milk) != Milk:
            return False

        shop_reg = self.__milk_counter.get(milk.barcode())
        if shop_reg is None:
            shop_reg = Shop.__ShopRegister(milk, 1, 100)
            self.__milk_counter[milk.barcode()] = shop_reg
        else:
            shop_reg.add_quantity(1)

    def buy_milk(self, barcode):
        shop_reg = self.__milk_counter[barcode]
        if shop_reg is not None:
            shop_reg.subtract_quantity(1)
            return shop_reg.milk
        return None

    class __ShopRegister(object):

        def __init__(self, milk, quantity, price):
            self.__milk = milk
            self.__quantity = quantity
            self.__price = price

        def milk(self, milk=None):
            if milk is None:
                return self.__milk
            elif type(milk) == Milk:
                self.__milk = milk
            else:
                return False

        def quantity(self, quantity=None):
            if quantity is None:
                return self.__quantity
            elif type(quantity) == int:
                self.__quantity = quantity
            else:
                return False

        def price(self, price=None):
            if price is None:
                return self.__price
            elif type(price) == int:
                self.__price = price
            else:
                return False

        def add_quantity(self, quantity):
            self.__quantity += quantity

        def subtract_quantity(self, quantity):
            self.__quantity -= quantity
