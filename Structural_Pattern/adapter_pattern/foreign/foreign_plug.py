from abc import ABC, abstractmethod


class ForeignPlug(ABC):

    @abstractmethod
    def plug_in(self): pass

    @abstractmethod
    def plug_out(self): pass
