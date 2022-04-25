from Creation.abstract_factory.farm.my_farm import MyFarm
from Creation.abstract_factory.owner.owner import Owner

if __name__ == '__main__':
    owner = Owner(MyFarm())

    owner.manage_my_farm()

