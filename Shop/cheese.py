from abc import ABCMeta
from datetime import datetime
from Shop.food import Food
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Cheese(Food):
    __metaclass__ = ABCMeta

    def __init__(self, barcode, weight, producer, best_before, fat_content):
        if not Cheese.check_data_can_represent_real_cheese(weight, fat_content):
            raise ValueError("Given data cannot represent real Cheese!")

        Food.__init__(self, barcode, producer, best_before)

        self.__weight = weight
        self.__fat_content = fat_content

    def weight(self):
        return self.__weight

    def fat_content(self):
        return self.__fat_content

    def __str__(self):
        return "Cheese{" + \
                "barcode: " + str(self.__barcode) + \
                ", weight: " + str(self.__weight) + " g" + \
                ", producer: '" + self.__producer + "'" + \
                ", best before: " + str(self.__best_before) + \
                ", fat content: " + str(self.__fat_content) + '}'

    @staticmethod
    def check_data_can_represent_real_cheese(weight, fat_content):
        if type(weight) != float:
            print("'cubic_capacity' must be float type!")
            return False
        elif type(fat_content) != float:
            print("'fat_content' must be float type!")
            return False
        return True
