# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Shop(object):

    def __init__(self, name, address, owner, milk_counter):
        if not Shop.check_data_can_represent_real_shop(name, address, owner, milk_counter):
            raise ValueError("Given data cannot represent a real Shop!")

        self.name = name
        self.address = address
        self.owner = owner
        self.milk_counter = milk_counter
        self.flag = milk_counter.length - 1

    @staticmethod
    def check_data_can_represent_real_shop(name, address, owner, milk_counter):
        if type(name) != str:
            print("'name' must be string type!")
            return False
        if type(address) != str:
            print("'address' must be string type!")
            return False
        if type(owner) != str:
            print("'owner' must be string type!")
            return False
        if type(milk_counter) != list:
            print("'milk_counter' must be list type!")
            return False
        return True

    def is_there_any_milk(self):
        return self.flag >= 0

    def buy_milk(self):
        self.flag -= 1
        return self.milk_counter[self.flag + 1]
