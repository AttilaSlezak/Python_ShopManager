from datetime import datetime
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Cheese(object):

    def __init__(self, barcode, weight, producer, best_before, fat_content):
        if not Cheese.check_data_can_represent_real_cheese(barcode, weight, producer, best_before, fat_content):
            raise ValueError("Given data cannot represent real Cheese!")

        self.__barcode = barcode
        self.__weight = weight
        self.__producer = producer
        self.__best_before = best_before
        self.__fat_content = fat_content

    def barcode(self):
        return self.__barcode

    def weight(self):
        return self.__weight

    def producer(self):
        return self.__producer

    def best_before(self):
        return self.__best_before

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
    def check_data_can_represent_real_cheese(barcode, weight, producer, best_before, fat_content):
        if type(barcode) != int:
            print("'barcode' must be integer type!")
            return False
        elif type(weight) != float:
            print("'cubic_capacity' must be float type!")
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