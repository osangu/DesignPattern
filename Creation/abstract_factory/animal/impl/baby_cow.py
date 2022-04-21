from ..abst.cow import Cow


class BabyCow(Cow):

    def __init__(self, name: str):
        print(f'new cow name : {name}')

    def meu(self):
        print(f'm..me..mue~~~')
