from abc import ABC,abstractmethod


class Dock(ABC):

    @abstractmethod
    def quack(self): pass