from Creational_Pattern.FactoryMethod.src.factory.factory_impl import FactoryImpl

if __name__ == '__main__':
    factory_impl = FactoryImpl()

    fride_chicken = factory_impl.create_product_by_order('fride')

    fride_chicken.print_type()

    source_chicken = factory_impl.create_product_by_order('source')

    source_chicken.print_type()

    barbecue_chicken = factory_impl.create_product_by_order('barbecue')

    barbecue_chicken.print_type()