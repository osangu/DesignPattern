from abc import ABC, abstractmethod


class Chicken(ABC):

    @abstractmethod
    def print_type(self): pass
