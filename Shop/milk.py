from abc import ABCMeta, abstractmethod
from Shop.food import Food
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Milk(Food):
    __metaclass__ = ABCMeta

    LITER = 1000
    HALF_LITER = 500
    GLASS = 200
    WHOLE_MILK = 2.8
    LOW_FAT_MILK = 1.5

    def __init__(self, barcode, cubic_capacity, producer, best_before, fat_content):

        if not Milk.check_data_can_represent_real_milk(cubic_capacity, fat_content):
            raise ValueError("Given data cannot represent real Milk!")

        Food.__init__(self, barcode, producer, best_before)

        self.__cubic_capacity = cubic_capacity
        self.__fat_content = fat_content

    def cubic_capacity(self):
        return self.__cubic_capacity

    def fat_content(self):
        return self.__fat_content

    def __str__(self):
        return "Milk{" + \
                "barcode: " + str(self.__barcode) + \
                ", cubic capacity: " + str(self.__cubic_capacity) + " ml" + \
                ", producer: '" + self.__producer + "'" + \
                ", best before: " + str(self.__best_before) + \
                ", fat content: " + str(self.__fat_content) + '}'

    @staticmethod
    def check_data_can_represent_real_milk(cubic_capacity, fat_content):
        if type(cubic_capacity) != int:
            print("'cubic_capacity' must be integer type!")
            return False
        elif type(fat_content) != float:
            print("'fat_content' must be float type!")
            return False
        return True
