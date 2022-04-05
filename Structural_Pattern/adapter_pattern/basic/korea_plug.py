from abc import ABC, abstractmethod


class KoreaPlug(ABC):

    @abstractmethod
    def stick(self): pass

    @abstractmethod
    def pull_out(self): pass
