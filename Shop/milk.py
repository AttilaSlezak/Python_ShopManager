from datetime import datetime
# -- coding: utf-8 --
__author__ = 'Slezak Attila'


class Milk(object):

    def __init__(self, cubic_capacity, producer, best_before, fat_content, price):

        if not Milk.check_data_can_represent_real_milk(cubic_capacity, producer, best_before, fat_content, price):
            raise ValueError("Given data cannot represent real Milk!")

        self.cubic_capacity = cubic_capacity
        self.producer = producer
        self.best_before = best_before
        self.fat_content = fat_content
        self.price = price

    def __str__(self):
        return "Milk{" + \
                "cubicCapacity: " + str(self.cubic_capacity) + " ml" + \
                ", producer: '" + self.producer + \
                ", bestBefore: " + str(self.best_before) + \
                ", fatContent: " + str(self.fat_content) + \
                ", price: " + str(self.price) + " forint(s)" + '}'

    @staticmethod
    def check_data_can_represent_real_milk(cubic_capacity, producer, best_before, fat_content, price):
        if type(cubic_capacity) != int:
            print("'cubic_capacity' must be integer type!")
            return False
        if type(producer) != str:
            print("'producer' must be string type!")
            return False
        if type(best_before) != datetime:
            print("'best_before' must be datetime type!")
            return False
        if type(fat_content) != float:
            print("'fat_content' must be float type!")
            return False
        if type(price) != int:
            print("'price' must be integer type!")
            return False
        return True

    def check_still_under_guarantee(self):
        return True if self.best_before > datetime.now() else False
