from datetime import datetime
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Milk(object):

    LITER = 1000
    HALF_LITER = 500
    GLASS = 200
    WHOLE_MILK = 2.8
    LOW_FAT_MILK = 1.5

    def __init__(self, barcode, cubic_capacity, producer, best_before, fat_content):

        if not Milk.check_data_can_represent_real_milk(barcode, cubic_capacity, producer, best_before, fat_content):
            raise ValueError("Given data cannot represent real Milk!")

        self.__barcode = barcode
        self.__cubic_capacity = cubic_capacity
        self.__producer = producer
        self.__best_before = best_before
        self.__fat_content = fat_content

    def barcode(self):
        return self.__barcode

    def cubic_capacity(self):
        return self.__cubic_capacity

    def producer(self):
        return self.__producer

    def best_before(self):
        return self.__best_before

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
    def check_data_can_represent_real_milk(barcode, cubic_capacity, producer, best_before, fat_content):
        if type(barcode) != int:
            print("'barcode' must be integer type!")
            return False
        elif type(cubic_capacity) != int:
            print("'cubic_capacity' must be integer type!")
            return False
        elif type(producer) != str:
            print("'producer' must be string type!")
            return False
        elif type(best_before) != datetime:
            print("'best_before' must be datetime type!")
            return False
        elif type(fat_content) != float:
            print("'fat_content' must be float type!")
            return False
        return True

    def check_still_under_guarantee(self):
        return True if self.__best_before > datetime.now() else False
