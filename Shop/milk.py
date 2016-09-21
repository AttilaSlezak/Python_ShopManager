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

        self.barcode = barcode
        self.cubic_capacity = cubic_capacity
        self.producer = producer
        self.best_before = best_before
        self.fat_content = fat_content

    def __str__(self):
        return "Milk{" + \
                "barcode: " + str(self.barcode) + \
                ", cubic capacity: " + str(self.cubic_capacity) + " ml" + \
                ", producer: '" + self.producer + "'" + \
                ", best before: " + str(self.best_before) + \
                ", fat content: " + str(self.fat_content) + '}'

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
        return True if self.best_before > datetime.now() else False
