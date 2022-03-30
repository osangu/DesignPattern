from src.factory.factory_abst import Factory

from src.chicken.chicken_impl import Fride, Source, Barbecue


class FactoryImpl(Factory):

    def create_product_by_order(self, order):
        operate_product = {
            'fride': Fride,
            'source': Source,
            'barbecue': Barbecue
        }

        return operate_product[order]()
