from .chicken import Chicken


class Fride(Chicken):

    def print_type(self):
        print('fride chicken')


class Source(Chicken):

    def print_type(self):
        print('source chicken')


class Barbecue(Chicken):

    def print_type(self):
        print('barbecue chicken')
