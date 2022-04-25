from Structure.bridge_pattern.platoon.solder import Solder


class Commander:

    def __init__(self, solder: Solder):
        self.solder = solder

    def command_fight(self):
        print('소대장 :: 전진!!')
        self.solder.fight()

    def command_make_encampment(self):
        print('소대장 :: 진지구축!!')
        self.solder.make_encampment()
