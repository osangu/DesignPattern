from ..farm.farm import Farm


class Owner:

    def __init__(self, farm: Farm):
        self.farm = farm


    def manage_my_farm(self):

        print('새로운 돼지가 태어나려고 한다!!')
        pig = self.farm.new_pig()
        pig.oink()

        print('\n새로운 오리가 태어나려고 한다!!')
        dock = self.farm.new_dock()
        dock.quack()

        print('\n새로운 소가 태어나려고 한다!!')
        cow = self.farm.new_cow()
        cow.meu()

