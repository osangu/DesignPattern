from ..abst.pig import Pig


class BabyPig(Pig):

    def __init__(self, name: str):
        print(f'new pig name : {name}')

    def oink(self):
        print(f'oi..oing...oin~nk!!')
