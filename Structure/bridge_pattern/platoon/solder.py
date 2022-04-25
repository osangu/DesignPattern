from abc import ABC,abstractmethod


class Solder(ABC):

    @abstractmethod
    def fight(self): pass

    @abstractmethod
    def make_encampment(self): pass