from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_product_by_order(self, order): pass
