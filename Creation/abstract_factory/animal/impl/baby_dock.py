from ..abst.dock import Dock


class BabyDock(Dock):

    def __init__(self,name: str):
        print(f'new dock name : {name}')

    def quack(self):
        print(f'qu..quac..quack!!')