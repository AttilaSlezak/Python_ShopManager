from Shop.milk import Milk
from Shop.cheese import Cheese
from Shop.food import Food
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

    def __is_there_any_certain_food(self, class_type):
        for one_shop_manager in self.__milk_counter.values():
            if isinstance(one_shop_manager.food(), class_type) and one_shop_manager.quantity() > 0:
                return True
        return False

    def is_there_any_milk(self):
        return self.__is_there_any_certain_food(Milk)

    def is_there_any_cheese(self):
        return self.__is_there_any_certain_food(Cheese)

    def replenish_food_counter(self, barcode, quantity):
        if type(quantity) != int:
            return False

        shop_reg = self.__milk_counter.get(barcode)
        if shop_reg is None:
            return False
        else:
            shop_reg.add_quantity(quantity)

    def add_new_food_to_food_counter(self, food, quantity, price):
        shop_reg = self.__ShopRegister(food, quantity, price)
        self.__milk_counter[food.barcode()] = shop_reg

    def remove_food_from_food_counter(self, barcode):
        self.__milk_counter.pop(barcode, None)

    def buy_milk(self, barcode, quantity):
        shop_reg = self.__milk_counter[barcode]
        if shop_reg is not None:
            shop_reg.subtract_quantity(quantity)

    class __ShopRegister(object):

        def __init__(self, food, quantity, price):

            if not self.check_data_can_represent_real_shop_register(food, quantity, price):
                raise ValueError("Given data cannot represent a real ShopRegister!")

            self.__food = food
            self.__quantity = quantity
            self.__price = price

        @staticmethod
        def check_data_can_represent_real_shop_register(food, quantity, price):
            if type(food) != Food:
                print("'cubic_capacity' must be Food type!")
                return False
            elif type(quantity) != int:
                print("'fat_content' must be integer type!")
                return False
            elif type(price) != int:
                print("'fat_content' must be integer type!")
                return False
            return True

        def food(self, food=None):
            if food is None:
                return self.__food
            elif type(food) == Food:
                self.__food = food
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
