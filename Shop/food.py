from abc import ABCMeta
from _datetime import datetime
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Food(object):
    __metaclass__ = ABCMeta

    def __init__(self, barcode, producer, best_before):
        if not Food.check_data_can_represent_real_food(barcode, producer, best_before):
            raise ValueError("Given data cannot represent real Food!")

        self.__barcode = barcode
        self.__producer = producer
        self.__best_before = best_before

    def barcode(self):
        return self.__barcode

    def producer(self):
        return self.__producer

    def best_before(self):
        return self.__best_before

    def __str__(self):
        return "Food{" + \
                "barcode: " + str(self.__barcode) + \
                ", producer: '" + self.__producer + "'" + \
                ", best before: " + str(self.__best_before) + '}'

    @staticmethod
    def check_data_can_represent_real_food(barcode, producer, best_before):
        if type(barcode) != int:
            print("'barcode' must be integer type!")
            return False
        elif type(producer) != str:
            print("'producer' must be string type!")
            return False
        elif type(best_before) != datetime:
            print("'best_before' must be datetime type!")
            return False
        return True

    def check_still_under_guarantee(self):
        return True if self.__best_before > datetime.now() else False